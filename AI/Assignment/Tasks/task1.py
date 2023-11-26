import random

def generate_chromosome():
    return [random.randint(0, 7) for _ in range(8)]

def generate_population(population_size):
    return [generate_chromosome() for _ in range(population_size)]

def fitness(chromosome):
    non_attacking_queens = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if (
                chromosome[i] != chromosome[j]
                and abs(chromosome[i] - chromosome[j]) != abs(i - j)
            ):
                non_attacking_queens += 1
    return non_attacking_queens

def crossover(parent1, parent2):
    crossover_point = random.randint(1, 6)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    mutation_point = random.randint(0, 7)
    new_gene = random.randint(0, 7)
    chromosome[mutation_point] = new_gene
    return chromosome

def select_parents(population):
    selected_parents = random.sample(population, 2)
    selected_parents.sort(key=lambda x: fitness(x), reverse=True)
    return selected_parents

def genetic_algorithm(population_size, termination_fitness):
    population = generate_population(population_size)
    
    generation = 1
    while True:
        population.sort(key=lambda x: fitness(x), reverse=True)
        fittest_chromosome = population[0]
        current_fitness = fitness(fittest_chromosome)
        
        if current_fitness >= termination_fitness:
            print("Solution found:")
            print("Chromosome:", fittest_chromosome)
            print("Fitness:", current_fitness)
            break
        
        new_population = [fittest_chromosome]

        for _ in range((population_size - 1) // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population
        generation += 1

        if generation % 10 == 0:
            print(f"Generation: {generation}, Fitness: {current_fitness}")

if __name__ == "__main__":
    genetic_algorithm(population_size=4, termination_fitness=26)
