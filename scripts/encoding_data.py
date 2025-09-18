from generate_data import generate_grid, place_word, search_word

import numpy as np
import pandas as pd
import string

# Create a dictionary mapping char to numbers
char_to_num = {char: idx for idx, char in enumerate(string.ascii_lowercase)}

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'grape', 'orange', 'peach']
    grid_size = 10
    grid, labels = generate_grid(n=grid_size, words=word_list)
    grid = np.array(grid)
    for word in word_list:
        place_word(grid, word)

    for label in labels:
        search_word(grid, label)
        
    # Encode the grid
    encoded_grid = np.zeros((grid_size, grid_size), dtype=int)
    for i in range(grid_size):
        for j in range(grid_size):
            encoded_grid[i, j] = char_to_num.get(grid[i][j], -1)
