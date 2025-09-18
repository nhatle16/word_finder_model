import random
import string

# Defined a fixed size (10 x 10) for the word grid
SIZE = 10

# Define possible directions
DIRECTIONS = [
    (0, 1),   # right
    (1, 0),   # down
    (1, 1),   # diagonal down-right
    (0, -1),  # left
    (-1, 0),  # up
    (-1, -1), # diagonal up-left
    (1, -1),  # diagonal down-left
    (-1, 1)   # diagonal up-right
]

# Simple word list
WORD_LIST = ["python", "java", "kotlin", "ruby", "swift", "go", "rust", "scala", "perl"]

def place_word(grid, word):
    n = len(grid)
    dx, dy = random.choice(DIRECTIONS)

    # Choose a random starting point
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)

    # Find the ending point
    end_x = x + dx * (len(word) - 1)
    end_y = y + dy * (len(word) - 1)


def generate_grid(n: int):
    grid = [[random.choice(string.ascii_lowercase) for _ in range(n)] for _ in range(n)]
    return grid

grid = generate_grid(SIZE)
for r in grid:
    for char in r:
        print(char, end=' ')
    print()