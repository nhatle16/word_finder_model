import ast
import numpy as np


if __name__ == "__main__":
    dataset = []
    with open("data.txt", "r") as f:
        for line in f:
            dataset.append(ast.literal_eval(line))
    
    # Prepare the data for training
    grids = np.array([sample['grid'] for sample in dataset])
    words = np.array([sample['word'] for sample in dataset])
    positions = np.array([sample['position'] for sample in dataset])