import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from sklearn.preprocessing import StandardScaler
from google.colab import files
from PIL import Image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

#PART 1

# Load dataset
df = pd.read_csv("/content/diabetes.csv")

# Display first 5 rows
print(df.head())

# Shape of dataset
print("Shape:", df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Features
X = df.drop("Outcome", axis=1)

# Target
y = df["Outcome"]

print("Feature Shape:", X.shape)
print("Target Shape:", y.shape)

#loading the MNIST Data

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train_norm = x_train.astype("float32") / 255.0
x_test_norm = x_test.astype("float32") / 255.0

normalized_pixel = x_train_norm[250]

print(x_train.shape)
print(x_test.shape)


print(x_train_norm.shape)

#PART 2

sample_image = x_train_norm[0:1]  # taking the first image as our sample image with dimension 28x28

#performing convolution and pooling on top of a sample image and then doing it on the entire data

sample_image = x_train_norm[0:1]  #taking the first image as our sample image with dimention 28X28

sample_conv = layers.Conv2D(filters=4, kernel_size=(3,3), activation='relu')

sample_pool = layers.MaxPooling2D(pool_size=(2,2))  #this pool size is same as window size 2x2

sample_image = np.expand_dims(sample_image, axis=-1)

conv_output = sample_conv(sample_image)

# n=28, f=3, so n-f+1 = 26x26
# dimention of feature map or the conv_output will be 26x26 represented as - [1,26,26,4] here 4 represents 4 filters

pool_output = sample_pool(conv_output)  #here since window size is 2x2, output dimention becomes 13x13

conv_output.shape

pool_output.shape

flatten_output = layers.Flatten()(pool_output)

flatten_output.shape

#Building the CNN Image Classifier

model = models.Sequential([
    layers.Input(shape=(28,28,1), name="input_layer"),
    layers.Conv2D(filters=16, kernel_size=(3,3), activation='relu', name="conv_layer_1"),
    layers.MaxPooling2D(pool_size=(2,2), name="pooling_layer_1"),  # output dimention - [1,13,13,16] = 2704 

    layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu', name="conv_layer_2"),
layers.MaxPooling2D(pool_size=(2,2), name="pooling_layer_2"),  # output dimention - [1,6,6,32] = 1152 values
    
    layers.Flatten(name="flatten_layer"),  # output dimention - [1,1152] = 1152 values

    layers.Dense(64, activation='relu', name="hidden_layer_1"), layers.Dense(32, activation='relu', name="hidden_layer_2"),

    layers.Dense(10, activation='softmax', name="output_layer")

])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


#PART 3
model.fit(x_train_norm, y_train, epochs=20)

test_loss, test_accuracy = model.evaluate(x_test_norm, y_test)

print("test accuracy", test_accuracy)

train_loss, train_accuracy = model.evaluate(x_train, y_train)

print("Training Accuracy:", train_accuracy)


#PART 4

y_pred_prob = model.predict(x_test_norm)
y_pred = np.argmax(y_pred_prob, axis=1)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)


cm = confusion_matrix(y_test, y_pred)

print(cm)
