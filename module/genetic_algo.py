import random

class GeneticAlgorithm:
    def __init__(self, roll, biscuits, population_size, generations, mutation_rate):
        self.roll = roll
        self.biscuits = biscuits
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def generate_individual(self):
        individual = []
        position = 0
        while position < self.roll.length:
            biscuit = random.choice(self.biscuits + [None])  # None represents no biscuit
            if biscuit is None or self.roll.check_position_empty(position, biscuit.length):
                individual.append((position, biscuit))
                position += 1 if biscuit is None else biscuit.length
            else:
                position += 1
        return individual

    def generate_population(self):
        return [self.generate_individual() for _ in range(self.population_size)]

    def fitness(self, individual):
        # Calculate the total value of biscuits in the individual
        return sum(biscuit.value for _, biscuit in individual if biscuit is not None)

    def select_parents(self, population):
        # Select individuals for reproduction based on their fitness
        weights = [self.fitness(individual) for individual in population]
        return random.choices(population, weights=weights, k=2)

    def crossover(self, parent1, parent2):
        # Combine two individuals to create a new individual
        crossover_point = random.randint(1, self.roll.length - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child

    def mutate(self, individual):
        # Randomly change an individual's biscuit placement
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                position, _ = individual[i]
                biscuit = random.choice(self.biscuits + [None])
                individual[i] = (position, biscuit)
        return individual

    def run(self):
        population = self.generate_population()

        for _ in range(self.generations):
            new_population = []
            for _ in range(self.population_size):
                parent1, parent2 = self.select_parents(population)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            population = new_population

        # Find the best solution
        best_individual = max(population, key=self.fitness)
        return best_individual, self.fitness(best_individual)

