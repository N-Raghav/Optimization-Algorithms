import random
import numpy as np
import matplotlib.pyplot as plt

# define function
def f(x):
    return x * np.sin(10 * np.pi * x) + 2

# define genetic algorithm parameters
POPULATION_SIZE = 50
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 5

# define the bounds for x
x_min = -1
x_max = 1

# define the fitness function
def fitness(x):
    return f(x)

# initialize population
def create_individual():
    return random.uniform(x_min, x_max)

population = [create_individual() for _ in range(POPULATION_SIZE)]

# define selection function using tournament selection
def tournament_selection(population, fitness_values, tournament_size):
    tournament_indices = np.random.choice(len(population), size=tournament_size, replace=False)
    tournament_fitnesses = [fitness_values[i] for i in tournament_indices]
    winner_index = tournament_indices[np.argmax(tournament_fitnesses)]
    return population[winner_index]

# define crossover function
def crossover(parent1, parent2):
    child1 = (parent1 + parent2) / 2.0
    child2 = (parent1 + parent2) / 2.0
    return child1, child2

# define mutation function
def mutate(individual):
    if random.random() < MUTATION_RATE:
        individual += random.uniform(-0.1, 0.1)
    return individual

# run the genetic algorithm
best_individuals = []
for generation in range(NUM_GENERATIONS):
    # evaluate fitness of individuals
    fitness_values = [fitness(individual) for individual in population]

    # select parents
    parents = [tournament_selection(population, fitness_values, tournament_size=TOURNAMENT_SIZE) for _ in range(POPULATION_SIZE)]

    # create offspring through crossover and mutation
    offspring = []
    for i in range(0, POPULATION_SIZE, 2):
        parent1 = parents[i]
        parent2 = parents[i+1]
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        offspring.append(child1)
        offspring.append(child2)

    # replace population with offspring
    population = offspring

    # record best individual
    best_individual = max(population, key=fitness)
    best_individuals.append(best_individual)

    # plot the current generation
    plt.clf() # clear previous plot
    xs = np.linspace(x_min, x_max, 1000)
    plt.plot(xs, f(xs), color='b', label='function')
    plt.scatter(population, fitness_values, color='g', label='population')
    plt.scatter(best_individual, fitness(best_individual), color='r', label='best individual')
    plt.legend()
    plt.title(f'Generation {generation+1}')
    plt.show()

# plot the fitness over generations
plt.plot(best_individuals)
plt.xlabel('Generation')
plt.ylabel('Best Individual Fitness')
plt.show()
