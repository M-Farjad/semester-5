import random

def generate_chromosome():
    return [random.randint(1, 8) for _ in range(8)]

def calculate_fitness(chromosome):
    conflicts = 0
    for i in range(7):
        for j in range(i + 1, 8):
            if chromosome[i] == chromosome[j] or abs(i - j) == abs(chromosome[i] - chromosome[j]):
                conflicts += 1
    return 28 - conflicts  # 28 is the maximum fitness achievable

def crossover(parent1, parent2):
    crossover_point = random.randint(1, 7)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    mutated_chromosome = chromosome.copy()
    mutation_point = random.randint(0, 7)
    new_position = random.randint(1, 8)
    mutated_chromosome[mutation_point] = new_position
    return mutated_chromosome

def genetic_algorithm(population_size, termination_fitness):
    population = [generate_chromosome() for _ in range(population_size)]

    generation = 0
    while True:
        population = sorted(population, key=lambda x: calculate_fitness(x), reverse=True)
        if calculate_fitness(population[0]) >= termination_fitness:
            print(f"Solution found in generation {generation}")
            print("Chromosome:", population[0])
            break

        new_population = []

        for _ in range(population_size // 2):
            parent1 = random.choice(population[:population_size // 2])
            parent2 = random.choice(population[:population_size // 2])

            child1, child2 = crossover(parent1, parent2)

            if random.random() < 0.1:
                child1 = mutate(child1)
            if random.random() < 0.1:
                child2 = mutate(child2)

            new_population.extend([child1, child2])

        population = new_population
        generation += 1

if __name__ == "__main__":
    genetic_algorithm(population_size=4, termination_fitness=26)
