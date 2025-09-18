import random
import string

# Defined a fixed size (10 x 10) for the word grid
SIZE = 10

def generate_grid(n: int):
    grid = [[random.choice(string.ascii_lowercase) for _ in range(n)] for _ in range(n)]
    return grid

grid = generate_grid(SIZE)
for r in grid:
    for char in r:
        print(char, end=' ')
    print()