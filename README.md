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
ssi-ml-project/
├── api/                              # Folder for the API setup and routes
│   └── app.py                        # Main Flask API code for predictions
├── saved_models/                     # Directory for saved models
│   ├── simple_nn_model.h5            # Trained simple neural network model
│   └── optimized_nn_model.h5         # Trained optimized neural network model
├── data/
│   └── SSI Data 2.csv                # Patient data for reference
├── .venv/                            # Virtual environment directory
└── README.md                         # Project documentation
Setup and Installation
1. Clone the Repository
Clone this project to your local machine:

bash
Copy code
git clone <https://github.com/Husnafazal/ssi-ml-project>
cd ssi-ml-project
2. Set Up the Virtual Environment
Create and activate a virtual environment to manage dependencies:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate     # On Windows
3. Install Requirements
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
4. Prepare the Dataset
Ensure the SSI Data 2.csv file is available in the data/ folder, as this is used for feature retrieval and one-hot encoding.

5. Run the API
Start the Flask API server:

bash
Copy code
flask --app api/app run
The API will be accessible at http://127.0.0.1:5000.

Using the API with Postman
The API accepts POST requests to provide predictions. You can use Postman to send requests and retrieve predictions from the models.

Structuring Input Data for Predictions
The input values in the JSON request represent the features that the model expects to receive. Each value must align with the data structure and preprocessing used during model training.

Understanding the Input Features
Feature Representation: Each value in the input array represents a specific feature from the original dataset, and they must be in the correct order.

Example: If your dataset included features such as age, blood pressure, and cholesterol level, an example input might look like this:

json
Copy code
{
    "input": [12, 120, 180]
}
12: represents age
120: represents blood pressure
180: represents cholesterol level
Replace these values with the actual patient data in the correct order and with any necessary transformations applied.

Preprocessing Steps: Make sure that input values reflect any transformations applied during training. For example, if you used one-hot encoding, scaling, or normalization, the input values should reflect these modifications.

Matching Feature Count: Ensure the input array has the same number of features as the model expects. If the model was trained with 297 features, the input array should contain exactly 297 values.

Example Input for Multiple Features
For a model trained with additional features, an input array might look like this:

json
Copy code
{
    "input": [12, 120, 180, 1, 0, 25, ...]  // Total 297 values
}
Sending a Request in Postman
URL: Set up a new POST request to http://127.0.0.1:5000/predict.

Request Body: In the Body section of Postman, select raw, choose JSON, and enter the following example input structure:

json
Copy code
{
  "input": [12, 120, 180]
}
Send the Request: Click "Send" in Postman.

Response: The response will include predictions from both models. Example response:

json
Copy code
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
Class: "At Risk of SSI" or "Not at Risk of SSI" to indicate the model’s prediction.
Probability: A confidence score from 0 to 1, with values closer to 1 indicating higher confidence in the prediction.
Deployment Plan
This API is currently set up for local deployment and testing using Postman.

Run the API on your local machine as described in the Setup and Installation section.
Use Postman to send requests and view model predictions.
In the future, the API could be deployed to a cloud hosting platform for remote access and integration with other applications.