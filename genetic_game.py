import sys
import random
from connect_4 import *
from genetic_pygame_utils import *
import pyglet as pg

# Initialize the gridcd
grid = Connect4Grid(900, 700)

# Parameters for Genetic Algorithm
population_size = 100
generations = 1000
crossover_prob = 0.7
mutation_prob = 0.1

# Initialize population
population = initialize_population(population_size)

# Main game loop
generation = 0
best_board = None
best_fitness = 0
optimal_found = False

def update(dt):
    global generation, best_board, best_fitness, optimal_found, population

    if  optimal_found or generation >= generations:
        return

    # Run one generation of Genetic Algorithm
    fitnesses = [fitness(board) for board in population]
    
    if max(fitnesses) == 42:
        print("Optimal solution found!")
        optimal_found = True
        grid.gen_label.text = f"Optimal Solution Found in {generation}th Generation"
        return

    parents = select_parents(population, fitnesses)
    next_population = []
    for i in range(0, population_size, 2):
        parent1, parent2 = parents[i], parents[i + 1]
        if random.random() < crossover_prob:
            child1, child2 = crossover(parent1, parent2)
        else:
            child1, child2 = parent1, parent2
        next_population.append(child1)
        next_population.append(child2)
    
    population = [mutate(board) if random.random() < mutation_prob else board for board in next_population]
    
    # Find best board in current generation
    best_fitness = 0
    for board in population:
        curr_fitness = fitness(board)
        if curr_fitness > best_fitness:
            best_fitness = curr_fitness
            best_board = board
    
    # Update the grid
    grid.update(generation, best_fitness)
    grid.draw_grid(best_board)
    
    generation += 1

if __name__ == "__main__":
    pg.clock.schedule_interval(update, 1/120.0)
    grid.run()