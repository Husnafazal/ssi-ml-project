SSI Prediction API
This project is a machine learning-based API that predicts the likelihood of Surgical Site Infection (SSI) in patients, using a Flask API to expose a trained model for real-time inference. The API allows users to input a patient's ID and receive predictions on whether they are at risk of SSI.

Project Overview
Purpose: The goal of this project is to provide healthcare professionals with a tool to assess the risk of SSI, using trained machine learning models.
Models Used: Two models were trained and deployed - a simple neural network model (simple_model) and an optimized neural network model (optimized_model). Each model generates a prediction on the likelihood of SSI.
Deployment: The API is deployed locally and can be accessed via Postman for demonstration and testing.
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
Clone this project to your local machine.

bash
Copy code
git clone <https://github.com/Husnafazal/ssi-ml-project>
cd ssi-ml-project
2. Set Up the Virtual Environment
Create and activate a virtual environment to manage dependencies.

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate     # On Windows
3. Install Requirements
Install the required Python packages.

bash
Copy code
pip install -r requirements.txt
4. Prepare the Dataset
Ensure the SSI Data 2.csv file is available in the data/ folder, as this is used for feature retrieval and one-hot encoding.

5. Run the API
Start the Flask API server.

bash
Copy code
flask --app api/app run
The API will be accessible at http://127.0.0.1:5000.

Using the API with Postman
Overview
Postman is used to interact with the API by sending a POST request with a patient ID to receive a prediction response.

Instructions
Open Postman and create a new POST request to:

arduino
Copy code
http://127.0.0.1:5000/predict
Request Body: In the Body section of Postman, select raw, choose JSON, and enter the following, replacing 411773 with any ID present in the dataset:

json
Copy code
{
  "input": [411773]
}
Send the Request: Click "Send" in Postman.

Review the Response: The response will include predictions from both models. Example response:

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
Class: "At Risk of SSI" or "Not at Risk of SSI" to indicate the model's decision.
Probability: A confidence score from 0 to 1, with values closer to 1 indicating higher confidence in the prediction.
Deployment Plan
This API is currently set up for local deployment and testing using Postman. For demonstration purposes:

Run the API on your local machine as described above.
Use Postman to send requests and view model predictions.
Future deployments could involve cloud hosting options to provide access via a public URL and support integration with other applications or services