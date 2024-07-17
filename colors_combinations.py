import random

color_themes = {
    "Ocean": {
        "GRID_COLOR": (0, 105, 148),  # Deep Blue
        "BACKGROUND_COLOR": (240, 248, 255),  # Alice Blue
        "FONT_COLOR": (0, 59, 92),  # Navy Blue
        "EMPTY_COLOR": (255, 255, 255),  # White
        "X_COLOR": (255, 140, 0),  # Dark Orange
        "O_COLOR": (0, 206, 209),  # Turquoise
        "BORDER_COLOR": (0, 59, 92)  # Navy Blue
    },
    "Forest": {
        "GRID_COLOR": (34, 139, 34),  # Forest Green
        "BACKGROUND_COLOR": (240, 255, 240),  # Honeydew
        "FONT_COLOR": (0, 100, 0),  # Dark Green
        "EMPTY_COLOR": (255, 255, 255),  # White
        "X_COLOR": (255, 140, 0),  # Dark Orange
        "O_COLOR": (65, 105, 225),  # Royal Blue
        "BORDER_COLOR": (139, 69, 19)  # Saddle Brown
    },
    "Sunset": {
        "GRID_COLOR": (70, 130, 180),  # Steel Blue
        "BACKGROUND_COLOR": (255, 228, 196),  # Bisque
        "FONT_COLOR": (139, 69, 19),  # Saddle Brown
        "EMPTY_COLOR": (255, 255, 255),  # White
        "X_COLOR": (220, 20, 60),  # Crimson
        "O_COLOR": (255, 165, 0),  # Orange
        "BORDER_COLOR": (70, 130, 180)  # Steel Blue
    },
    "Pastel": {
        "GRID_COLOR": (176, 196, 222),  # Light Steel Blue
        "BACKGROUND_COLOR": (255, 240, 245),  # Lavender Blush
        "FONT_COLOR": (105, 105, 105),  # Dim Gray
        "EMPTY_COLOR": (255, 255, 255),  # White
        "X_COLOR": (255, 182, 193),  # Light Pink
        "O_COLOR": (173, 216, 230),  # Light Blue
        "BORDER_COLOR": (188, 143, 143)  # Rosy Brown
    },
    "High Contrast": {
        "GRID_COLOR": (50, 50, 50),  # Dark Gray
        "BACKGROUND_COLOR": (240, 240, 240),  # Light Gray
        "FONT_COLOR": (0, 0, 0),  # Black
        "EMPTY_COLOR": (255, 255, 255),  # White
        "X_COLOR": (255, 0, 0),  # Red
        "O_COLOR": (0, 0, 255),  # Blue
        "BORDER_COLOR": (0, 0, 0)  # Black
    },
    "Neon": {
        "GRID_COLOR": (0, 0, 0),  # Black
        "BACKGROUND_COLOR": (25, 25, 25),  # Very Dark Gray
        "FONT_COLOR": (255, 255, 255),  # White
        "EMPTY_COLOR": (50, 50, 50),  # Dark Gray
        "X_COLOR": (255, 0, 255),  # Magenta
        "O_COLOR": (0, 255, 0),  # Lime
        "BORDER_COLOR": (0, 255, 255)  # Cyan
    },
    "Earth Tones": {
        "GRID_COLOR": (139, 69, 19),  # Saddle Brown
        "BACKGROUND_COLOR": (245, 222, 179),  # Wheat
        "FONT_COLOR": (101, 67, 33),  # Dark Brown
        "EMPTY_COLOR": (255, 248, 220),  # Cornsilk
        "X_COLOR": (205, 133, 63),  # Peru
        "O_COLOR": (107, 142, 35),  # Olive Drab
        "BORDER_COLOR": (160, 82, 45)  # Sienna
    },
    "Cool Blues": {
        "GRID_COLOR": (70, 130, 180),  # Steel Blue
        "BACKGROUND_COLOR": (240, 248, 255),  # Alice Blue
        "FONT_COLOR": (25, 25, 112),  # Midnight Blue
        "EMPTY_COLOR": (255, 255, 255),  # White
        "X_COLOR": (0, 191, 255),  # Deep Sky Blue
        "O_COLOR": (30, 144, 255),  # Dodger Blue
        "BORDER_COLOR": (0, 0, 128)  # Navy
    },
    "Warm Reds": {
        "GRID_COLOR": (178, 34, 34),  # Firebrick
        "BACKGROUND_COLOR": (255, 250, 240),  # Floral White
        "FONT_COLOR": (139, 0, 0),  # Dark Red
        "EMPTY_COLOR": (255, 255, 255),  # White
        "X_COLOR": (255, 99, 71),  # Tomato
        "O_COLOR": (255, 140, 0),  # Dark Orange
        "BORDER_COLOR": (128, 0, 0)  # Maroon
    }
}

# To select a random theme:
random_theme = random.choice(list(color_themes.keys()))
selected_theme = color_themes[random_theme]

print(f"Selected theme: {random_theme}")
for color_name, color_value in selected_theme.items():
    print(f"{color_name}: {color_value}")