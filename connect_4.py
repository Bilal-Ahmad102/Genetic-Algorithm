import random
from connect_4_utils import *
from genetic_pygame import *

# Initialize the population with random boards
def initialize_population(size):
    population = []
    for _ in range(size):
        population.append(generateRandomState())
    return population

# Fitness function
def fitness(board, player='x'):
    if player == 'o':
        opponent = 'x'
    else:
        opponent = 'o'
    fit = 0
    for i in range(42):
        if i%2==0 and board[i] == player :
           fit+=1
        if i%2==1 and board[i] == opponent:
            fit+=1
    return fit 
        
# Selection using roulette wheel selection
def select_parents(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    parents = random.choices(population, probabilities, k=len(population))
    return parents

# Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, 41)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation
def mutate(board):
    index = random.randint(0, 41)
    
    if board[index] == 'x':
        board[index] = 'o'
    else:
        board[index] = 'x'
        
    return board

# Genetic Algorithm
def genetic_algorithm(population_size, generations, crossover_prob, mutation_prob):
    population = initialize_population(population_size)
    print("Initial population:")
    for i in population:
        draw_grid(i)
    
    for generation in range(generations):
        print(f"\nGeneration {generation + 1}")
        fitnesses = [fitness(board) for board in population]
        
        if max(fitnesses) == 41:
            print("Optimal solution found!")
            break  # Solution found
        
        for idx, board in enumerate(population):
            print(f"Board {idx + 1} Fitness: {fitnesses[idx]}")
            printState(board)
        
        # Selection
        parents = select_parents(population, fitnesses)
        
        # Crossover
        next_population = []
        for i in range(0, population_size, 2):
            parent1, parent2 = parents[i], parents[i + 1]
            if random.random() < crossover_prob:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            next_population.append(child1)
            next_population.append(child2)
        
        # Mutation
        population = [mutate(board) if random.random() < mutation_prob else board for board in next_population]
    
    # Final best solution
    best_fitness = 0
    best_board = None
    for board in population:
        current_fitness = fitness(board)
        
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_board = board
    
    return best_board

# Parameters
population_size = 100
generations = 1000
crossover_prob = 0.7
mutation_prob = 0.1

# Running the Genetic Algorithm
# best_board = genetic_algorithm(population_size, generations, crossover_prob, mutation_prob)
# print(f"Best board state found, Fitness{fitness(best_board)}:")
# printState(best_board)

# board = initialize_population(5)
# for i in board:
#     print(f"Board fitness {fitness(i)}:\n")
#     printBoard(i)