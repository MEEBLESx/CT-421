Code Structure:

-Global Variables

-Representation function
  In all classes other than the BinPacking class it creates a binary string of a certain length that contains random choices between 0 and 1
  
-Fitness Function
  In the OneMaxProblem we get the sum of the binary string, as we know that if all are ones then the fitness/sum will be 30.
  In the TargetString we check if elements are matching if so we add 1 to our matching count and then returning this matching count.
  In the DeceptiveLandscape we check if 1 is in the solution if so it returns the sum of the solution if not we return 2 times the length of the solution (60)
  

-Mutate Function
 Is the same across all classes except the BinPacking class,
 We create a copy of the solution given we then itterate over the length of the mutated_solution and check if a random number is less than our mutate
 variable, if so we then switch from 1 -> 0 or 0 -> 1 this is also known as bitwise mutation.

 -Crossover Function
  Takes in two variables p1/parent1 and p2/parent2, a random crossover point is then selected and using this we generate two children from 
  the cross over point and the parents.

  -Selection Function
    I use a tournament selection which firstly selects 3 random canditates from the population, it then checks the fitness for each, 
    the candidate with the largest fitness is the winner and is then appended onto selected_parents

  -Genetic Algorithm
    This is the base of the algorithm where all calls to other functions are made, We first call our representation function to create
    our series of bitstrings, then we calculate our fitness using these bit strings, once we have calculated the fitness it then begins 
    the selection process. Once that completes we fill a new population with a mutated population. Once finished it returns the avg_fitness.
