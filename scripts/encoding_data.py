from generate_data import generate_grid, search_word

import numpy as np
import string

# Create a dictionary mapping char to numbers
char_to_num = {char: idx for idx, char in enumerate(string.ascii_lowercase)}

def encode_grid(grid: np.ndarray) -> np.ndarray:
    n = grid.shape[0]
    encoded = np.full((n, n), -1, dtype=int)

    for y in range(n):
        for x in range(n):
            encoded[y, x] = char_to_num.get(grid[y, x], -1)

    return encoded

def encode_word(word, max_len=10) -> np.ndarray:
    word = word.lower()
    arr = np.full((max_len,), fill_value=-1, dtype=np.int32)
    for i, char in enumerate(word):
        if i < max_len:
            arr[i] = char_to_num[char]
    return arr

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'grape', 'orange', 'peach']
    grid_size = 10
    grid, labels = generate_grid(n=grid_size, words=word_list)
    for label in labels:
        search_word(grid, label)

    grid = np.array(grid)
    encoded_grid = encode_grid(grid)

    print(encoded_grid)
    print(encode_word('apple'))