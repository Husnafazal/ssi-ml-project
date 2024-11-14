<<<<<<< HEAD
# Surgical Site Infection (SSI) Prediction API

This project is a machine learning-based API designed to predict the likelihood of Surgical Site Infection (SSI) in patients. It uses a Flask API to expose a trained model, providing real-time predictions based on patient data inputs. This tool aims to help healthcare professionals assess SSI risk effectively.

## Project Overview

- **Purpose**: Provides healthcare professionals with a tool to assess SSI risk in patients.
- **Models**: Utilizes two neural network models:
  - `simple_model` (basic model)
  - `optimized_model` (optimized for improved accuracy)
- **Deployment**: Set up for local testing via Postman.

## Project Structure

```plaintext
=======
SSI Prediction API

This project is a machine learning-based API that predicts the likelihood of Surgical Site Infection (SSI) in patients. It uses a Flask API to expose a trained model for real-time inference. The API allows users to input a patient's data and receive predictions on whether they are at risk of SSI.

Project Overview

Purpose: Provide healthcare professionals with a tool to assess the risk of SSI using trained machine learning models.
Models Used: Two neural network models:
simple_model: A straightforward neural network.
optimized_model: An enhanced neural network with improved accuracy.
Deployment: The API is deployed locally and can be accessed via Postman for testing.
Project Structure
graphql
Copy code
>>>>>>> e71d797e3417b59b71f865632012601f32b419a2
ssi-ml-project/
├── api/                              # API setup and routes
│   └── app.py                        # Flask API code for predictions
├── saved_models/                     # Directory for saved models
│   ├── simple_nn_model.h5            # Trained simple neural network model
│   └── optimized_nn_model.h5         # Trained optimized neural network model
├── data/
│   └── SSI Data 2.csv                # Dataset for reference
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
Ensure the SSI Data 2.csv file is available in the data/ folder. This file is essential for feature retrieval and input formatting
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
    "class": "At Risk of SSI",
    "probability": 0.87
  },
  "simple_model_prediction": {
    "class": "Not at Risk of SSI",
    "probability": 0.35
  }
}
Interpreting Results
Class: "At Risk of SSI" or "Not at Risk of SSI", indicating the model’s prediction.
Probability: A confidence score from 0 to 1, with values closer to 1 indicating higher confidence.
Deployment Plan
This API is currently set up for local deployment and testing. For broader deployment, consider hosting on a cloud platform to provide public access and allow integration with other applications.

<<<<<<< HEAD
=======
Run the API on your local machine as described in the Setup and Installation section.
Use Postman to send requests and view model predictions.
In the future, the API could be deployed to a cloud hosting platform for remote access and integration with other applications.
>>>>>>> e71d797e3417b59b71f865632012601f32b419a2
