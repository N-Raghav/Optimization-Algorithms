import random
import math

# Define the objective function
def f(x):
    return math.sin(x)

# Define PSO parameters
POPULATION_SIZE = 100
MAX_ITERATIONS = 50
C1 = 2.0
C2 = 2.0
W = 0.7
X_MIN = 0
X_MAX = math.pi

# Define Particle class
class Particle:
    def __init__(self):
        self.position = random.uniform(X_MIN, X_MAX)
        self.velocity = 0
        self.best_position = self.position

    def evaluate_fitness(self):
        return f(self.position)

    def update_velocity(self, global_best_position):
        r1 = random.random()
        r2 = random.random()
        cognitive_component = C1 * r1 * (self.best_position - self.position)
        social_component = C2 * r2 * (global_best_position - self.position)
        self.velocity = W * self.velocity + cognitive_component + social_component

    def update_position(self):
        self.position += self.velocity
        if self.position < X_MIN:
            self.position = X_MIN
        elif self.position > X_MAX:
            self.position = X_MAX

# Define PSO function
def pso():
    # Initialize particles
    particles = [Particle() for _ in range(POPULATION_SIZE)]

    # Initialize global best position
    global_best_position = particles[0].position
    global_best_fitness = f(global_best_position)

    # Run PSO
    for iteration in range(MAX_ITERATIONS):
        # Update particles
        for particle in particles:
            fitness = particle.evaluate_fitness()
            if fitness > f(particle.best_position):
                particle.best_position = particle.position
            if fitness > global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particle.position
            particle.update_velocity(global_best_position)
            particle.update_position()

        # Print current best position and fitness
        print(f'Iteration {iteration+1}: Global Best Position = {global_best_position:.6f}, Global Best Fitness = {global_best_fitness:.6f}')

    return global_best_position, global_best_fitness

# Run PSO and print results
best_position, best_fitness = pso()
print(f'Best Position = {best_position:.6f}, Best Fitness = {best_fitness:.6f}')
