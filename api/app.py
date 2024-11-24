from pathlib import Path
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# Load the saved models
simple_model_path = Path(__file__).parent.parent / "saved_models/simple_nn_model.keras"
optimized_model_path = Path(__file__).parent.parent / "saved_models/optimized_nn_model.keras"
simple_model = load_model(simple_model_path)
optimized_model = load_model(optimized_model_path)

# Load the dataset
csv_file = Path(__file__).parent.parent / "data/SSI Data.csv"
data = pd.read_csv(csv_file)

# Initialize the encoder for categorical features
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoder.fit(data.select_dtypes(include=['object']))  # Fit the encoder to categorical columns

# Function to get feature values by ID and preprocess them
def get_feature_values_by_id(id_number):
    row = data[data['ID'] == id_number]
    if not row.empty:
        feature_values = row.values[0][1:]  # Exclude ID and return all features
        return feature_values
    else:
        return None

# Function to preprocess the input features
def preprocess_input(feature_values):
    # Convert to DataFrame for easier processing
    feature_df = pd.DataFrame([feature_values], columns=data.columns[1:])
    
    # One-hot encode categorical features
    encoded_features = encoder.transform(feature_df.select_dtypes(include=['object']))
    
    # Combine numeric and encoded features
    numeric_features = feature_df.select_dtypes(exclude=['object']).values
    processed_input = np.concatenate([numeric_features, encoded_features], axis=1)
    
    return processed_input

# Define a function to convert model outputs into human-readable format
def format_prediction(class_prediction, probability):
    if class_prediction == 1:
        return {
            "class": "At Risk of SSI",
            "probability": float(probability[0])  # Ensure it's a float for JSON serialization
        }
    else:
        return {
            "class": "Not at Risk of SSI",
            "probability": float(probability[0])  # Ensure it's a float for JSON serialization
        }

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()
    input_data = np.array(data['input']).reshape(1, -1)

    # Check if input_data has fewer than 297 features, pad if necessary
    if input_data.shape[1] < 297:
        padding = np.zeros((1, 297 - input_data.shape[1]))
        input_data = np.concatenate([input_data, padding], axis=1)

    # Make sure the input data has the correct data type
    input_data = input_data.astype(np.float32)

    # Make prediction using the model
    simple_pred = simple_model.predict(input_data)
    optimized_pred = optimized_model.predict(input_data)

       # Formatting predictions
    simple_prediction = format_prediction(np.round(simple_pred[0]).astype(int), simple_pred)
    optimized_prediction = format_prediction(np.round(optimized_pred[0]).astype(int), optimized_pred)

    return jsonify({
        "optimized_model_prediction": optimized_prediction,
        "simple_model_prediction": simple_prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
