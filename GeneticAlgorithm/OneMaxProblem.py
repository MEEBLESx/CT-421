import random
import numpy as np
import matplotlib.pyplot as plt

pop_size = 100
string_length = 30
r_mut = 0.01
generations = 100


def gen_rand_binary_string(length):
    result = []
    for i in range(length):
        result.append(random.choice([0, 1]))
    return result

def calculate_fitness(solution):
    #only need to sum as we can assume that the maximum fitness will be the string_length which is 30 and if it contains only 1s it will have a fitness of 30.
    return sum(solution)

def mutate(solution, r_mut):
    mutated_solution = solution.copy()
    for i in range(len(mutated_solution)):
        if random.random() < r_mut:
            mutated_solution[i] = 1 - solution[i]
    return mutated_solution


def crossover(p1, p2):
    crossover_point = random.randint(1, len(p1) - 1)
    child1 = p1[:crossover_point] + p2[crossover_point:]
    child2 = p2[:crossover_point] + p1[crossover_point:]
    return child1, child2

#was using a fitness based selection but achieved too low scores.
def selection(population, fitness_scores, tournament_size=3):
    selected_parents = []

    for i in range(len(population)):
        tournament_candidates = random.sample(range(len(population)), tournament_size)
        index_of_winner = tournament_candidates[0]

        for candidate in tournament_candidates[1:]:
            if fitness_scores[candidate] > fitness_scores[index_of_winner]:
                index_of_winner = candidate

        selected_parents.append(population[index_of_winner])
    return selected_parents

def genetic_algorithm(population_size, string_length, r_mut, generations):

    population = []
    for i in range(population_size):
        population.append(gen_rand_binary_string(string_length))
    avg_fitness = []

    for generation in range(generations):
        fitness_scores = [calculate_fitness(solution) for solution in population]
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

    return avg_fitness


def plot_average_fitness(avg_fitness):
    generations = range(1, len(avg_fitness) + 1)
    plt.plot(generations, avg_fitness, label='Average Fitness')
    plt.xlabel('Generations')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness Over Generations One Max Problem')
    plt.legend()
    plt.show()

avg_fitness = genetic_algorithm(pop_size, string_length, r_mut, generations)

plot_average_fitness(avg_fitness)


best_fitness = max(avg_fitness)
print(f"The best fitness value is: {best_fitness}")
