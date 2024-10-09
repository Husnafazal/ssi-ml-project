from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import os

app = Flask(__name__)

# Ensure the path is correct
MODEL_DIR = os.path.join(os.getcwd(), 'saved_models')
simple_model_path = os.path.join(MODEL_DIR, 'simple_nn_model.h5')
optimized_model_path = os.path.join(MODEL_DIR, 'optimized_nn_model.h5')

# Load the saved models
simple_model = load_model('saved_models/simple_nn_model.h5')
optimized_model = load_model('saved_models/optimized_nn_model.h5')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.array(data['input']).reshape(1, -1)

    if input_data.shape[1] < 297:
        padding = np.zeros((1, 297 - input_data.shape[1]))
        input_data = np.concatenate([input_data, padding], axis=1)

    # Make sure the input data has the correct data type
    input_data = input_data.astype(np.float32)

    # Make prediction using the simple model
    simple_pred = simple_model.predict(input_data)
    optimized_pred = optimized_model.predict(input_data)

    threshold = 0.5
    optimized_class = 1 if optimized_pred[0] >= threshold else 0
    simple_class = 1 if simple_pred[0] >= threshold else 0

    return jsonify({
        'simple_model_prediction': {
            'probability': simple_pred[0].tolist(),
            'class': simple_class
        },
        'optimized_model_prediction': {
            'probability': optimized_pred[0].tolist(),
            'class': optimized_class
        }
    })


if __name__ == '__main__':
    app.run(debug=True)
