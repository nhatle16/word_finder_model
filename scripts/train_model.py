import ast
import numpy as np
import tensorflow as tf

from tensorflow.keras import layers, models

if __name__ == "__main__":
    dataset = []
    with open("data.txt", "r") as f:
        for line in f:
            dataset.append(ast.literal_eval(line))
    
    # Prepare the data for training
    grids = np.array([sample['grid'] for sample in dataset])
    words = np.array([sample['word'] for sample in dataset])
    positions = np.array([sample['position'] for sample in dataset])

    # Reshape grids into a 4D tensor for CNN and combine with words into a single input
    grids = grids.reshape((-1, 10, 10, 1))

    # Create a tensor for words
    words_tensor = np.zeros(grids.shape[0], 10, 10, 1)
    words_tensor[:, 0, :, 1] = words

    input_data = np.concatenate(grids, words_tensor, axis=-1)
    