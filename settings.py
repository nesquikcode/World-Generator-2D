# world generation
ITERATIONS = 200
COLUMNS = 200
ROWS = 200

# generator settings
WATER_ITERATIONS = 128
SUBWATER_ITERATIONS = 8
FOREST_ITERATIONS = 64
MOUNTAINS_ITERATIONS = 128
HIGH_MOUNTAINS_ITERATIONS = 132
SNOW_ITERATIONS = 8
FINAL_ITERATIONS = 1 # not available
MOUNTAINS_CHANCE = "1:8000" # spawn chance less than 1:1000 may look unnatural
HIGH_MOUNTAINS_CHANCE = "1:8000"
SNOW_CHANCE = "1:3"
DIRTCHANCE = "1:2"
FORESTCHANCE = "1:2"

# window size (for disable PIL rescaling on saved image use parameters equal to columns and rows. if you cant open large window set 'CONSOLE_MODE' to True.)
WIDTH = 800
HEIGHT = 800

# don't change, parameters for view
BLOCKX = WIDTH/COLUMNS
BLOCKY = HEIGHT/ROWS

# colors
DIRT = (139, 194, 74)
DARKDIRT = (83, 140, 45)
WATER = (33, 150, 255)
SUBWATER = (3, 190, 255)
SAND = (255, 231, 70)
MOUNTAINS = (100, 102, 93)
HIGH_MOUNTAINS = (88, 89, 84)
SNOW = (214, 219, 216)

# other params
ENABLE_LOAD_CALLBACK = True
CONSOLE_MODE = False # not available