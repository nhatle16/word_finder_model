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

    # Create input layer, 2 convolution layers, 1 flatten layer and 2 dense (neurons are fully connected) layers
    input_data = layers.Input(shape=(10, 10, 2), name="input")
    conv1 = layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', name="conv-layer1")(input_data)
    conv2 = layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', name="conv-layer2")(conv1)
    flatten = layers.Flatten(name="flatten")(conv2)
    dense1 = layers.Dense(128, activation='relu', name="hidden1")
    output = layers.Dense(4, activation='relu', name="hidden2")

    # Model compiling and training
    model = models.Model(inputs=input_data, outputs=output)
    model.compile(optimizer="adam", loss="mean_squared_error", metrics=['accuracy'])
    model.fit(input_data, positions, epochs=500, batch_size=32, verbose=1)

    model.summary()