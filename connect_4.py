import random
from connect_4_utils import *

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

