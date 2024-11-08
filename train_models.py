import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import SGD, Adam
import pathlib

# Load the dataset
ssi_data = pd.read_csv(pathlib.Path(__name__).resolve().parent / 'data/SSI Data 2.csv')

# One-hot encode categorical columns
object_columns = ssi_data.select_dtypes(include=['object']).columns
for col in object_columns:
    encoder = OneHotEncoder(sparse_output=False)
    encoded_data = encoder.fit_transform(ssi_data[[col]])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out([col]))
    ssi_data = ssi_data.drop(col, axis=1).reset_index(drop=True)
    ssi_data = pd.concat([ssi_data, encoded_df], axis=1)

# Replace non-numeric values with NaN and fill with 0
ssi_data = ssi_data.replace(' ', np.nan).fillna(0)

# Define features (X) and target (y)
X = ssi_data.drop('SSI', axis=1)  # Replace 'SSI' with the actual target column name
y = ssi_data['SSI']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a function to create and train models with different optimizers
def train_and_evaluate_model(optimizer, model_name):
    model = Sequential([
        Input(shape=(X_train.shape[1],)),  # Use Input layer for defining the input shape
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')  # Output layer for binary classification
    ])

    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

    # Save the model in the new .keras format
    save_path = f'saved_models/{model_name}.keras'
    model.save(save_path)
    print(f'Model saved to {save_path}')

# Ensure the directory for saved models exists
if not os.path.exists('saved_models'):
    os.makedirs('saved_models')

# Train and save models with different optimizers
train_and_evaluate_model(SGD(learning_rate=0.01), 'simple_nn_model')
train_and_evaluate_model(Adam(learning_rate=0.001), 'optimized_nn_model')
