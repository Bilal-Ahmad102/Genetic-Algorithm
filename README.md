# Genetic Algorithm for Connect 4

## Overview

This project implements a genetic algorithm to find an optimal or near-optimal solution for a Connect 4 game state. The algorithm simulates the evolution of game boards over several generations, selecting the fittest boards, performing crossover, and applying mutations to generate new populations. The goal is to find a board state that maximizes a specified fitness function.

## Files and Directories

- `main.py`: The main script that runs the genetic algorithm and displays the game state using Pygame.
- `connect_4_utils.py`: Utility functions for generating random game states and printing the board.
- `genetic_pygame_utils.py`: Pygame utilities for drawing the Connect 4 grid and managing the display.
- `README.md`: This readme file.

## Requirements

- Python 3.6 or higher
- Pygame

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/connect4-genetic-algorithm.git
   ```
2. Navigate to the project directory:
   ```
   cd connect4-genetic-algorithm
   ```
3. Install the required dependencies:
   ```
   pip install pygame
   ```

## Running the Project

1. Execute the main script:
   ```
   python main.py
   ```
2. The Pygame window will open, displaying the evolution of the game states. The best fitness and generation number will be displayed on the screen.

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

### Genetic Algorithm Execution

- `genetic_algorithm(population_size, generations, crossover_prob, mutation_prob)`: Runs the genetic algorithm for a specified number of generations.

## Pygame Display

### Drawing the Grid

- `draw_grid(state)`: Draws the Connect 4 grid with the current game state on the Pygame window.

### Displaying Information

- The generation number and best fitness are displayed at the top of the Pygame window.

## Parameters

- `population_size`: Number of boards in the population.
- `generations`: Number of generations to run the genetic algorithm.
- `crossover_prob`: Probability of performing crossover.
- `mutation_prob`: Probability of performing mutation.

## Screenshots

### Initial Population
![Initial Population](Genetic/ScreenShots/Initial_Population.png)

### Midway through Generations
![Midway Generation](Genetic/ScreenShots/Midway_Population.png)

### Optimal Solution Found
![Optimal Solution](Genetic/ScreenShots/Optimal_Population.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Pygame: For providing the library to create the graphical interface.
- OpenAI: For the inspiration and tools to implement the genetic algorithm.

## Contact

For any inquiries or suggestions, please contact [your email].
