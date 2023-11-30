import random

# Simple genetic algorithm
def generate_individual():
    return [random.randint(0, 1) for _ in range(8)]

def fitness(individual):
    # Example fitness function (sum of bits)
    return sum(individual)

def genetic_algorithm(population_size, generations):
    population = [generate_individual() for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        new_population = population[:population_size // 2]

        for _ in range(population_size // 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            crossover_point = random.randint(1, len(parent1) - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            new_population.append(child)

        population = new_population

    return max(population, key=fitness)

# Usage
result_individual = genetic_algorithm(population_size=10, generations=100)
print("Result from genetic algorithm:", result_individual)