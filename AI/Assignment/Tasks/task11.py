import random

def generate_chromosome():
    return [random.randint(0, 7) for _ in range(8)]

def generate_population(population_size):
    return [generate_chromosome() for _ in range(population_size)]

def fitness(chromosome):
    return sum(chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == abs(i - j) for i in range(8) for j in range(i + 1, 8))

def crossover(parent1, parent2):
    crossover_point = random.randint(1, 6)
    return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]

def mutate(chromosome):
    mutation_point = random.randint(0, 7)
    chromosome[mutation_point] = random.randint(0, 7)
    return chromosome

def select_parents(population):
    return sorted(random.sample(population, 2), key=lambda x: fitness(x), reverse=True)

def genetic_algorithm(population_size, termination_fitness):
    population = generate_population(population_size)
    
    for generation in range(1, 1000):  # Limited to 1000 generations for simplicity
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

        if generation % 10 == 0:
            print(f"Generation: {generation}, Fitness: {current_fitness}")

if __name__ == "__main__":
    genetic_algorithm(population_size=4, termination_fitness=26)
