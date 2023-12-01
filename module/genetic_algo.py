import random

class GeneticAlgorithm:
    def __init__(self, roll, biscuits, population_size, generations, mutation_rate):
        """
        Initializes the Genetic Algorithm for optimizing biscuit placement on a roll.

        Parameters:
        roll (Roll): The roll of dough to be used.
        biscuits (list): List of available biscuit types.
        population_size (int): The number of individuals in each generation.
        generations (int): The total number of generations to evolve.
        mutation_rate (float): The probability of mutation in each individual.
        """
        self.roll = roll
        self.biscuits = biscuits
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def generate_individual(self):
        """
        Generates a single individual for the population. An individual is a potential solution
        representing a specific arrangement of biscuits on the roll.

        Returns:
        list: A list of tuples, each representing a biscuit and its position on the roll.
        """
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
        """
        Generates the initial population for the algorithm, consisting of multiple individuals.

        Returns:
        list: A list of individuals, each representing a potential solution.
        """
        return [self.generate_individual() for _ in range(self.population_size)]

    def fitness(self, individual):
        """
        Calculates the fitness of an individual. Fitness is determined by the total value
        of biscuits placed on the roll.

        Parameters:
        individual (list): An individual solution from the population.

        Returns:
        int: The fitness value of the individual.
        """
        idx = 0
        cmp = 0
        while idx < len(individual):
            _, biscuit = individual[idx]
            if biscuit == None :
                idx += 1
            else :
                cmp += biscuit.value
                idx += biscuit.length - 1

        return cmp

    def select_parents(self, population):
        """
        Selects a pair of parents for reproduction based on their fitness.

        Parameters:
        population (list): The current population of individuals.

        Returns:
        tuple: Two selected individuals from the population.
        """
        weights = [self.fitness(individual) for individual in population]
        return random.choices(population, weights=weights, k=2)

    def crossover(self, parent1, parent2):
        """
        Performs crossover between two parents to produce a new individual.

        Parameters:
        parent1, parent2 (list): The parent individuals.

        Returns:
        list: A new individual resulting from the crossover of the parents.
        """
        crossover_point = random.randint(1, self.roll.length - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child

    def mutate(self, individual):
        """
        Applies mutation to an individual. Mutation randomly alters the biscuit placement.

        Parameters:
        individual (list): An individual to be mutated.

        Returns:
        list: The mutated individual.
        """
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                position, _ = individual[i]
                biscuit = random.choice(self.biscuits + [None])
                individual[i] = (position, biscuit)
        return individual

    def run(self):
        """
        Runs the genetic algorithm over a number of generations to find the best solution.

        Returns:
        tuple: The best individual found and its fitness value.
        """
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

