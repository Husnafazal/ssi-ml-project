from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# Load the saved models
simple_model = load_model('saved_models/simple_nn_model.h5')
optimized_model = load_model('saved_models/optimized_nn_model.h5')

# Load the dataset
data = pd.read_csv('../data/SSI Data 2.csv')

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
    data_input = request.get_json()

    # Ensure the input is valid
    if 'id' not in data_input:
        return jsonify({"error": "ID is required"}), 400

    id_number = data_input['id']
    feature_values = get_feature_values_by_id(id_number)

    if feature_values is None:
        return jsonify({"error": "ID not found"}), 404

    # Preprocess the feature values
    input_data = preprocess_input(feature_values)

    # Debugging: Print input data shape and type
    print("Input data for prediction:", input_data)
    print("Input data shape:", input_data.shape)

    # Make predictions using both models
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
