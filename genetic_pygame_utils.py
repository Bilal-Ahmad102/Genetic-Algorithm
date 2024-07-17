import pyglet
from pyglet.gl import *
from pyglet import shapes
from connect_4_utils import generateRandomState
from colors_combinations import selected_theme

class Connect4Grid:
    def __init__(self, width, height):
        self.window = pyglet.window.Window(width, height, "7x6 Circle Grid")
        self.batch = pyglet.graphics.Batch()
        self.label_batch = pyglet.graphics.Batch()
        self.shapes = []
        self.labels = []
        self.generation_num = 0
        self.best_one = 0
        
        # Constants
        self.WIDTH, self.HEIGHT = width, height
        self.ROWS, self.COLS = 6, 7
        self.PADDING_RATIO = 0.015  # 1.5% of window width
        self.GRID_WIDTH_RATIO = 0.9  # 80% of window width
        self.GRID_HEIGHT_RATIO = 0.8  # 80% of window height
        self.BORDER_THICKNESS_RATIO = 0.015  # 1.5% of window width

        # Colors 
        self.colors = selected_theme
        self.GRID_COLOR = self.colors["GRID_COLOR"]  
        self.BACKGROUND_COLOR = self.colors["BACKGROUND_COLOR"] 
        self.FONT_COLOR = self.colors["FONT_COLOR"]
        self.EMPTY_COLOR = self.colors["EMPTY_COLOR"]
        self.X_COLOR = self.colors["X_COLOR"]
        self.O_COLOR = self.colors["O_COLOR"]
        self.border_color = self.colors["BORDER_COLOR"]        

        # Define font
        self.font_size = int(self.HEIGHT * 0.04)  # 4% of window height
        self.font = 'Arial'

        self.window.event(self.on_draw)

    def draw_grid(self, state):
        self.shapes.clear()
        self.labels.clear()

        # Draw the background
        self.shapes.append(shapes.Rectangle(0, 0, self.WIDTH, self.HEIGHT, color=self.BACKGROUND_COLOR, batch=self.batch))
        
        # Calculate grid dimensions
        grid_width = self.WIDTH * self.GRID_WIDTH_RATIO
        grid_height = self.HEIGHT * self.GRID_HEIGHT_RATIO
        self.CIRCLE_RADIUS = min(grid_width / (self.COLS * 2 + 2), grid_height / (self.ROWS * 2 + 2))
        self.PADDING = self.WIDTH * self.PADDING_RATIO

        # Calculate grid position (right bottom corner)
        grid_x = self.WIDTH - grid_width - self.PADDING
        grid_y = self.PADDING

        # Draw border
        border_thickness = self.WIDTH * self.BORDER_THICKNESS_RATIO
        self.shapes.append(shapes.Rectangle(
            grid_x - border_thickness, 
            grid_y - border_thickness, 
            grid_width + 2 * border_thickness, 
            grid_height + 2 * border_thickness, 
            color=self.border_color, 
            batch=self.batch
        ))
    
        # Draw grid background
        self.shapes.append(shapes.Rectangle(grid_x, grid_y, grid_width, grid_height, color=self.GRID_COLOR, batch=self.batch))
        
        # Draw the circles
        for row in range(self.ROWS):
            for col in range(self.COLS):
                x = grid_x + (col + 0.5) * (grid_width / self.COLS)
                y = grid_y + (row + 0.5) * (grid_height / self.ROWS)
                index = row * self.COLS + col
                if state[index] == 'x':
                    color = self.X_COLOR
                elif state[index] == 'o':
                    color = self.O_COLOR
                else:
                    color = self.EMPTY_COLOR
                self.shapes.append(shapes.Circle(x, y, self.CIRCLE_RADIUS * 0.8, color=color, batch=self.batch))
        
        # Draw the column labels (A-G) at the top
        column_labels = 'ABCDEFG'
        for col in range(self.COLS):
            label_x = grid_x + (col + 0.5) * (grid_width / self.COLS)
            label_y = grid_y + grid_height +20+ self.font_size / 2
            self.labels.append(pyglet.text.Label(column_labels[col], font_name=self.font, font_size=self.font_size,
                                                color=self.FONT_COLOR + (255,), x=label_x, y=label_y,
                                                anchor_x='center', anchor_y='center', batch=self.label_batch))
        
        # Draw the row labels (1-6)
        for row in range(self.ROWS):
            label_x = grid_x - 10-self.font_size / 2
            label_y = grid_y + (row + 0.5) * (grid_height / self.ROWS)
            self.labels.append(pyglet.text.Label(str(self.ROWS - row), font_name=self.font, font_size=self.font_size,
                                                 color=self.FONT_COLOR + (255,), x=label_x, y=label_y,
                                                 anchor_x='center', anchor_y='center', batch=self.label_batch))
        print("pl")
        self.labels.append(pyglet.text.Label(f"Generation : {self.generation_num}     Best One : {self.best_one}", 
                                             font_name=self.font, font_size=self.font_size,
                                                 color=self.FONT_COLOR + (255,), x=self.WIDTH/2, y=self.HEIGHT-40,
                                                 anchor_x='center', anchor_y='center', batch=self.label_batch))

    def on_draw(self):
        self.window.clear()
        self.batch.draw()
        self.label_batch.draw()
    
    def update(self,gen_num,best_one):
        self.generation_num = gen_num
        self.best_one = best_one

    def run(self):
        pyglet.app.run()

