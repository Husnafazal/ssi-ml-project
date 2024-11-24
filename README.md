

## Project Structure

SSI Prediction API

This project is a machine learning-based API that predicts the likelihood of Surgical Site Infection (SSI) in patients. It uses a Flask API to expose a trained model for real-time inference. The API allows users to input a patient's data and receive predictions on whether they are at risk of SSI.

Project Overview

Purpose: Provide healthcare professionals with a tool to assess the risk of SSI using trained machine learning models.
Models Used: Two neural network models:
simple_model: A straightforward neural network.
optimized_model: An enhanced neural network with improved accuracy.
Deployment: The API is deployed locally and can be accessed via Postman for testing.
Project Structure
```plaintext


ssi-ml-project/
├── api/                              # API setup and routes
│   └── app.py                        # Flask API code for predictions
├── saved_models/                     # Directory for saved models
│   ├── simple_nn_model.keras         # Trained simple neural network model
│   └── optimized_nn_model.keras      # Trained optimized neural network model
├── data/
│   └── SSI Data.csv                  # Dataset for reference
├── .venv/                            # Virtual environment directory
└── README.md                         # Project documentation

Setup and Installation

1. Clone the Repository
git clone https://github.com/Husnafazal/ssi-ml-project
cd ssi-ml-project
2. Set Up the Virtual Environment
Create and activate a virtual environment to manage dependencies.
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate     # On Windows
3. Install Requirements
Install the required Python packages.
pip install -r requirements.txt
4. Prepare the Dataset
Ensure the SSI Data.csv file is available in the data/ folder. This file is essential for feature retrieval and input formatting
5. Run the API
Start the Flask API server.
flask --app api/app run
The API will be accessible at http://127.0.0.1:5000.
Using the API with Postman
The API can be accessed by sending a POST request through Postman.

Endpoint for Prediction
URL: http://127.0.0.1:5000/predict
Method: POST
Content-Type: JSON

Request Body Format
The API expects input data in the form of patient features, represented as an array of values. These values should be ordered to match the features used during model training. Below is an example:
{
  "input": [12, 23, 78]
}
Understanding the Input Format
Each value in the input array corresponds to specific patient features used by the model. For example:

12 could represent age
23 could represent blood pressure
78 could represent cholesterol level
Ensure that the number of values and their order match the feature set used for training.

Example Postman Request
Open Postman and create a new POST request.

Set the URL to http://127.0.0.1:5000/predict.

In the Body section of Postman, select raw, choose JSON, and enter the patient data:
{
  "input": [12, 23, 78]
}
Click "Send" to send the request.
Example Response
The response includes predictions from both the simple and optimized models. Here is an example output:
{
    "optimized_model_prediction": {
        "class": "Not at Risk of SSI",
        "probability": 0.0011039716191589832
    },
    "simple_model_prediction": {
        "class": "Not at Risk of SSI",
        "probability": 0.4138723313808441
    }
}
Interpreting Results
Class: "At Risk of SSI" or "Not at Risk of SSI", indicating the model’s prediction.
Probability: A confidence score from 0 to 1, with values closer to 1 indicating higher confidence.


Deployment Plan
http://13.233.46.164:8000/predict
# Flask App on AWS EC2

This is a Flask application deployed on an AWS EC2 instance, accessible at: **[http://13.233.46.164:8000/predict](http://13.233.46.164:8000/predict)**

## Deployment Steps
1. Launch an Ubuntu EC2 instance, open ports 22 and 8000.
2. Install dependencies: `sudo apt update && sudo apt install python3 python3-pip git -y`
3. Clone the repository: `git clone <repository-url> && cd <repository-folder>`
4. Set up environment: `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
5. Start the app: `gunicorn --bind 0.0.0.0:8000 app:app`

## Usage
- **Endpoint:** `/predict`
- **Method:** POST
- **Input:** JSON payload
- **Response:** Prediction results in JSON format

Run the API on your local machine as described in the Setup and Installation section.
Use Postman to send requests and view model predictions.
