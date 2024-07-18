# Genetic Algorithm for Connect 4

## Overview

This project implements a genetic algorithm to find an optimal or near-optimal solution for a Connect 4 game state. The algorithm simulates the evolution of game boards over several generations, selecting the fittest boards, performing crossover, and applying mutations to generate new populations. The goal is to find a board state that maximizes a specified fitness function.

## Files and Directories

- `genetic_game.py`: The main script that runs the genetic algorithm and displays the game state using Pyglet.
- `connect_4.py`: Contains the core genetic algorithm functions.
- `connect_4_utils.py`: Utility functions for generating random game states and printing the board.
- `genetic_game_utils.py`: Pyglet utilities for drawing the Connect 4 grid and managing the display.
- `README.md`: This readme file.

## Requirements

- Python 3.6 or higher
- Pyglet

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Bilal-Ahmad102/Genetic-Algorithm
   ```
2. Navigate to the project directory:
   ```
   cd Genetic-Algorithm
   ```
3. Install the required dependencies:
   ```
   pip install pyglet
   ```

## Running the Project

1. Execute the main script:
   ```
   python genetic_game.py
   ```
2. The Pyglet window will open, displaying the evolution of the game states. The best fitness and generation number will be displayed on the screen.

## Genetic Algorithm Components

### Initialization

- `initialize_population(size)`: Generates an initial population of random game boards.

### Fitness Function

- `fitness(board, player='x')`: Evaluates the fitness of a game board based on the number of desired positions for the player and the opponent.

### Selection

- `select_parents(population, fitnesses)`: Selects parents for the next generation using roulette wheel selection.

### Crossover

- `crossover(parent1, parent2)`: Performs crossover between two parent boards to generate two child boards.

### Mutation

- `mutate(board)`: Randomly mutates a single position on the board.

## Pyglet Display

### Drawing the Grid

- `draw_grid(state)`: Draws the Connect 4 grid with the current game state on the Pyglet window.

### Displaying Information

- The generation number and best fitness are displayed at the top of the Pyglet window.

## Parameters

- `population_size`: Number of boards in the population.
- `generations`: Number of generations to run the genetic algorithm.
- `crossover_prob`: Probability of performing crossover.
- `mutation_prob`: Probability of performing mutation.

## Screenshots
### Initial Population
![Initial Population](https://github.com/Bilal-Ahmad102/Genetic-Algorithm/blob/main/ScreenShots/Initial_Population.png)

### Midway through Generations
![Midway Generation](https://github.com/Bilal-Ahmad102/Genetic-Algorithm/blob/main/ScreenShots/Midway_Population.png)

### Optimal Solution Found
![Optimal Solution](https://github.com/Bilal-Ahmad102/Genetic-Algorithm/blob/main/ScreenShots/Optimal_Population.png)



## Acknowledgements

- Pyglet: For providing the library to create the graphical interface.

## Contact

For any inquiries or suggestions, please contact [ba2736180@gmail.com].