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

    # Make prediction using the simple model
    simple_pred = simple_model.predict(input_data)
    optimized_pred = optimized_model.predict(input_data)

    return jsonify({
        'simple_model_prediction': simple_pred[0].tolist(),
        'optimized_model_prediction': optimized_pred[0].tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)
