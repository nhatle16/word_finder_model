from generate_data import generate_grid, place_word
from encoding_data import encode_grid, encode_word

import numpy as np
import random
import string

def generate_sample(n, max_word_len=10):
    # Generate a grid and a random word, then put it in the grid
    grid = [['' for _ in range(n)] for _ in range(n)]
    word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3,max_word_len)))
    pos = place_word(grid, word)
    # Place random letters in empty cells
    for y in range(n):
        for x in range(n):
            if grid[y][x] == '':
                grid[y][x] = random.choice(string.ascii_lowercase)
    return grid, word, pos

def create_dataset(num_samples=2000, grid_size=10, max_word_len=10):
    dataset = []

    # Create data samples
    for _ in range(num_samples):
        grid, word, (sx, sy, dx, dy) = generate_sample(n=grid_size, max_word_len=6)
        word_data = [[word, (sx, sy, dx, dy)], encode_word(word)]
        dataset.append([encode_grid(np.array(grid)), word_data])

    return dataset

if __name__ == "__main__":
   dataset = create_dataset(num_samples=10)
   for sample in dataset:
       print(sample)