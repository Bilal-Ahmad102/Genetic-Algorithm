import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 900, 700
ROWS, COLS = 6, 7
CIRCLE_RADIUS = 40
PADDING = 10
GRID_COLOR = (0, 150, 255)  # Blue grid background
BACKGROUND_COLOR = (245, 222, 179)  # Light tan background for the window
FONT_COLOR = (0, 0, 0)  # Black font color
EMPTY_COLOR = (255, 255, 255)  # White color for empty slots
X_COLOR = (255, 0, 0)  # Red color for 'x'
O_COLOR = (0, 0, 255)  # Blue color for 'o'

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("7x6 Circle Grid")

# Define font
font = pygame.font.SysFont(None, 36)

def draw_grid(state):
    # Draw the blue grid background
    grid_width = COLS * (2 * CIRCLE_RADIUS + PADDING) + PADDING
    grid_height = ROWS * (2 * CIRCLE_RADIUS + PADDING) + PADDING
    grid_x = (WIDTH - grid_width) // 2
    grid_y = (HEIGHT - grid_height) // 2
    pygame.draw.rect(screen, GRID_COLOR, (grid_x, grid_y, grid_width, grid_height))
    
    # Draw the circles    
    for row in range(ROWS):
        for col in range(COLS):
            x = grid_x + col * (2 * CIRCLE_RADIUS + PADDING) + CIRCLE_RADIUS + PADDING // 2
            y = grid_y + row * (2 * CIRCLE_RADIUS + PADDING) + CIRCLE_RADIUS + PADDING // 2
            
            index = row * COLS + col
            if state[index] == 'x':
                color = X_COLOR
            elif state[index] == 'o':
                color = O_COLOR
            else:
                color = EMPTY_COLOR
            
            pygame.draw.circle(screen, color, (x, y), CIRCLE_RADIUS)
    
    # Draw the column labels (A-G) separately
    column_labels = 'ABCDEFG'
    for col in range(COLS):
        label = font.render(column_labels[col], True, FONT_COLOR)
        label_x = grid_x + col * (2 * CIRCLE_RADIUS + PADDING) + CIRCLE_RADIUS + PADDING // 2 - label.get_width() // 2
        label_y = grid_y - label.get_height() - 5
        screen.blit(label, (label_x, label_y))

    # Draw the row labels (1-6)
    for row in range(ROWS):
        label = font.render(str(ROWS - row), True, FONT_COLOR)
        label_x = grid_x - label.get_width() - 5
        label_y = grid_y + row * (2 * CIRCLE_RADIUS + PADDING) + CIRCLE_RADIUS + PADDING // 2 - label.get_height() // 2
        screen.blit(label, (label_x, label_y))

