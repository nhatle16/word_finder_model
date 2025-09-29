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
    words_tensor = np.zeros((grids.shape[0], 10, 10, 1))
    words_tensor[:, 0, :, 0] = words

    # Stacked the grids and words tensors
    combined_input= np.concatenate([grids, words_tensor], axis=-1)

    # Create input layer and 2 convolution layers
    input_data = layers.Input(shape=(10, 10, 2), name='input')
    conv1 = layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu')(input_data)
    conv2 = layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu')(conv1)

    model = models.Sequential(name="crossword_solver")
    model.summary()