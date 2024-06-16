import pygame
import sys
import random
from connect_4 import *
from genetic_pygame import *

# Initialize Pygame
pygame.init()


# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("7x6 Circle Grid")

# Define font
font = pygame.font.SysFont(None, 36)

# Parameters for Genetic Algorithm
population_size = 100
generations = 1000
crossover_prob = 0.7
mutation_prob = 0.1

# Initialize population
population = initialize_population(population_size)

# Main game loop
running = True
generation = 0
best_board = None
optimal_found = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Run one generation of Genetic Algorithm
    fitnesses = [fitness(board) for board in population]
    
    if max(fitnesses) == 42:
        print("Optimal solution found!")
        optimal_found = True
        break  # Solution found
    
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
        current_fitness = fitness(board)
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_board = board

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the grid
    draw_grid(best_board)

    # Display generation number and best fitness
    text = font.render(f"Generation: {generation + 1} ", True, FONT_COLOR)
    screen.blit(text, (10, 10))
    text = font.render(f"Best Fitness: {best_fitness}", True, FONT_COLOR)
    screen.blit(text, (240, 10))

    # Update the display
    pygame.display.flip()

    generation += 1

    # Add time delay
    pygame.time.delay(200)  # Delay for 200 milliseconds (0.2 seconds)

if optimal_found:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with the background color
        screen.fill(BACKGROUND_COLOR)

        # Draw the grid
        draw_grid(best_board)

        # Display generation number and best fitness
        text = font.render(f"Optimal solution found!", True, FONT_COLOR)
        screen.blit(text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Add time delay to prevent high CPU usage
        pygame.time.delay(100)

# Quit Pygame
pygame.quit()
sys.exit()
