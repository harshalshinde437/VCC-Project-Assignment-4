# Virtualization and Cloud Computing Project
- **Group Members**:
- **Harshal Shinde - G23AI2045**
- **Diksha Mehra - G23AI2017**
- **Aishwarya Salunkhe - G23AI2031**

# Credit Card Fraud Detection

## Overview
This project is a machine learning-based web application for detecting fraudulent credit card transactions. The model is trained on a dataset of credit card transactions and uses logistic regression to predict whether a transaction is fraudulent or not. The frontend of the application is built using Django, and the model is served through a REST API. The entire application is containerized using Docker and deployed on Google Cloud Platform (GCP) Kubernetes.

## Features
- Predicts whether a credit card transaction is fraudulent based on 30 features, including `Time`, `Amount`, and anonymized transaction data (`V1` to `V28`).
- User-friendly interface built with Django and Bootstrap.
- Containerized using Docker for easy deployment and scalability.
- Deployed on GCP Kubernetes for high availability and load balancing.

## Table of Contents
1. [Technologies Used](#technologies-used)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Model Explanation](#model-explanation)
6. [Deployment](#deployment)
7. [Future Enhancements](#future-enhancements)
8. [Contributors](#contributors)

## Technologies Used

- **Django**: Web framework for the frontend and backend of the application.
- **Python**: Core programming language used for machine learning and backend logic.
- **Sklearn**: Library used to build and train the logistic regression model.
- **Pandas & Numpy**: Data handling and manipulation libraries for working with the dataset.
- **Joblib**: Used for saving and loading the trained machine learning model.
- **Docker**: For containerizing the application.
- **Kubernetes (GCP)**: For deploying and managing the application in a production environment.

## Dataset
The dataset used for this project is the publicly available [Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud) from Kaggle. It contains anonymized transaction data with the following features:
- `Time`, `Amount`: Transaction details.
- `V1` to `V28`: Principal component analysis (PCA) transformed features.
- `Class`: The target variable, where `1` indicates a fraudulent transaction and `0` indicates a legitimate transaction.

## Installation

### Prerequisites
- Python 3.10 or higher
- Docker
- Google Cloud SDK (for Kubernetes deployment)

### Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/harshalshinde437/Credit_card_fraud_detection
   cd fraud-detection-app
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate the Database**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Application**:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit `http://127.0.0.1:8000/`.

## Usage

1. Enter the transaction details such as `Time`, `Amount`, and values for `V1` to `V28` in the form.
2. Click on "Predict" to get the result of whether the transaction is legitimate or fraudulent.
3. The application will display the prediction result along with the entered values.

## Model Explanation

The machine learning model used in this project is a logistic regression classifier that has been trained using the train-test split method.

- **Logistic Regression**: A statistical model that is typically used for binary classification tasks. It estimates the probability of a binary outcome.
- **Train-Test Split**: The dataset was split into training and testing datasets in an 80-20 ratio. The model was trained on 80% of the data and validated on the remaining 20%.

## Deployment

### Docker

1. **Build Docker Image**:
   ```bash
   docker build -t fraud-detection-app .
   ```

2. **Run Docker Container**:
   ```bash
   docker run -p 8000:8000 fraud-detection-app
   ```

### Kubernetes (GCP)

1. **Push Docker Image to Google Container Registry**:
   ```bash
   docker tag fraud-detection-app gcr.io/[PROJECT_ID]/fraud-detection-app:latest
   docker push gcr.io/[PROJECT_ID]/fraud-detection-app:latest
   ```

2. **Create Kubernetes Cluster**:
   ```bash
   gcloud container clusters create fraud-detection-cluster --num-nodes=3
   ```

3. **Deploy the Application**:
   Apply the Kubernetes deployment and service YAML files:
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

4. **Access the Application**:
   Get the external IP from your service and open it in a browser to access the application.

## Future Enhancements

1. **Improved Model Accuracy**: Enhance the machine learning model by experimenting with different algorithms (e.g., Random Forest, SVM).
2. **Real-time Detection**: Integrate real-time fraud detection using streaming data from payment systems.
3. **User Authentication**: Add user authentication for restricted access to sensitive parts of the application.
4. **Logging and Monitoring**: Implement logging and monitoring for better error tracking and performance analysis.
5. **Scalability**: Implement horizontal scaling on Kubernetes to handle increased traffic load.

## Contributors

- **Group Members**:
- **Harshal Shinde**
- **Diksha Mehra**
- **Aishwarya Salunkhe**

## License

This project is licensed under the IIT License.
