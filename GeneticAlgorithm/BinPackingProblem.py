import random
import numpy as np
import matplotlib.pyplot as plt

pop_size = 5
string_length = 1
r_mut = 0.01
generations = 1000
bin_capacity = 1000
current_bin_capacity = -1
total_bins = 1
pop = []
all_of_them = []

def gen_rand_binary_string(data):
    data_copy = data[:]
    random.shuffle(data_copy)
    result = data_copy
    return result


def calculate_fitness(solution, bin_cap):
    global total_bins
    global bin_capacity
    global pop
    all_bin_cap = []
    current_cap = bin_cap

    current_bin = []

    for item_size in solution:
        if item_size <= current_cap:
            current_cap -= item_size
            current_bin.append(item_size)
        else:
            total_bins += 1
            pop.append(current_bin)
            all_bin_cap.append(current_cap)
            current_cap = bin_capacity
            current_bin = [item_size]

    if current_cap != bin_cap:
        pop.append(current_bin)

    return sum(all_bin_cap)


def mutate(solution, r_mut):
    mutated_solution = solution.copy()
    length = len(mutated_solution)
    if random.random() < r_mut:
        indices = list(range(length))
        random.shuffle(indices)

        for i in range(length):
            mutated_solution[i] = mutated_solution[indices[i]]

    return mutated_solution

def crossover(p1, p2):
    crossover_point = random.randint(1, len(p1) - 1)
    child1 = p1[:crossover_point] + p2[crossover_point:]
    child2 = p2[:crossover_point] + p1[crossover_point:]
    return child1, child2


# was using a fitness based selection but achieved too low scores.
def selection(population, fitness_scores, tournament_size=3):
    selected_parents = []
    for i in range(len(population)):
        tournament_candidates = random.sample(range(len(population)), tournament_size)
        index_of_winner = tournament_candidates[0]  # Assume the first candidate is the winner initially

        for candidate in tournament_candidates[1:]:
            if fitness_scores[candidate] < fitness_scores[index_of_winner]:
                index_of_winner = candidate

        selected_parents.append(population[index_of_winner])

    return selected_parents


def genetic_algorithm(population_size, r_mut, generations, data):
    global total_bins
    global all_of_them
    all_bins = []
    population = []
    for i in range(population_size):
        population.append(gen_rand_binary_string(data))

    avg_fitness = []

    for generation in range(generations):
        fitness_scores = []
        for solution in population:
            fitness_scores.append(calculate_fitness(solution, bin_capacity))
            all_bins.append(total_bins)
            total_bins = 1

        average_fitness = np.mean(fitness_scores)
        avg_fitness.append(average_fitness)

        selected = selection(population, fitness_scores)

        new_population = []
        while len(new_population) < population_size:
            p1 = random.choice(selected)
            p2 = random.choice(selected)
            c1, c2 = crossover(p1, p2)
            c1 = mutate(c1, r_mut)
            c2 = mutate(c2, r_mut)
            new_population.extend([c1, c2])

        population = new_population

    pop.clear()
    print(min(all_bins))
    return avg_fitness


def plot_average_fitness(avg_fitness):
    generations = range(1, len(avg_fitness) + 1)
    plt.plot(generations, avg_fitness, label='Average Fitness')
    plt.xlabel('Generations')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness Over Generations')
    plt.legend()
    plt.show()


result = {}
title = []
with open('Binpacking-2 (1).txt', 'r') as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        title_line = lines[i].strip()
        title.append(title_line)
        # move to next line
        i += 1

        number = int(lines[i].strip())
        i += 1

        data = []
        for _ in range(number):
            line = lines[i].split(',')
            data.extend([int(line[0])] * int(line[1]))
            i += 1
        # save the title and data associated with it
        result[title[len(title) - 1]] = data

for x in range(len(title)):
        avg_fitness = genetic_algorithm(pop_size, r_mut, generations, result[title[x]])
        plot_average_fitness(avg_fitness)

