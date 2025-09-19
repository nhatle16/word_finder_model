from generate_data import generate_grid
from encoding_data import encode_grid, encode_word
import numpy as np

def create_dataset(num_samples=2000, grid_size=10, word_list=None, max_word_len=10):
    grids = []
    for _ in range(num_samples):
        grid, labels = generate_grid(n=grid_size, words=word_list)
        encoded_grid = encode_grid(np.array(grid))
        grids.append((encoded_grid, labels))
    return grids

if __name__ == "__main__":
    WORD_LIST = ['apple', 'banana', 'grape', 'orange', 'peach']
    dataset = create_dataset(num_samples=5, grid_size=10, word_list=WORD_LIST)
    print("Sample encoded grid:")
    print(dataset[0][0])