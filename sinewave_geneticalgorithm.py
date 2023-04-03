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

# define selection function using Roulette Wheel
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probs = [fitness_value/total_fitness for fitness_value in fitness_values]
    selected_index = np.random.choice(len(population), p=selection_probs)
    return population[selected_index]

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
    parents = [roulette_wheel_selection(population, fitness_values) for _ in range(POPULATION_SIZE)]

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

# plot the best individual over generations
xs = np.linspace(-1, 1, 1000)
ys = f(xs)
plt.plot(xs, ys, label='f(x)')

for i in range(0, NUM_GENERATIONS, 10):
    ys = [f(x) for x in [best_individuals[i]]]
    plt.scatter([best_individuals[i]], ys, marker='x', color='red', s=50, label=f'gen {i}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function f(x) = xsin(10πx) + 2 with Genetic Algorithm and Roulette Wheel Selection')
plt.show()
