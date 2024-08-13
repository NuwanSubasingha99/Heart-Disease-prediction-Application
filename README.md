# Heart Disease Prediction Project

## Overview

This project is an end-to-end machine learning application designed to predict the likelihood of heart disease in patients based on medical data. It involves data preprocessing, model training, API development, and a user-friendly interface for making predictions.

## Key Features

### 1. Data Preprocessing
- Utilizes Pandas and Scikit-Learn to clean, scale, and encode the dataset.
- Ensures the data is ready for training and prediction.

### 2. Model Training
- Trained multiple models including Random Forest, Logistic Regression, and SVM.
- Hyperparameter tuning using GridSearchCV for optimal performance.
- Final model saved using Pickle for later use in predictions.

### 3. Flask API Development
- Created a RESTful API using Flask to serve the trained model.
- Handles input data, makes predictions, and returns results in real-time.

### 4. User Interface (UI)
- Designed a responsive web interface using HTML, CSS, and JavaScript.
- Users can input medical data to get predictions on heart disease risk.
- Validation and error handling implemented for better user experience.

## Installation

### Prerequisites
- Python 3.6+
- Flask
- Scikit-Learn
- Pandas
- Numpy

## Usage

1. Open the UI in your web browser.
2. Input the required medical details into the form fields.
3. Click "Predict" to submit the data and receive a prediction on heart disease risk.

## Example JSON Request
To test the prediction API directly, you can send a JSON request like this:
```json
{
    "age": 57,
    "sex": 1,
    "cp": 2,
    "trestbps": 150,
    "chol": 276,
    "fbs": 0,
    "restecg": 1,
    "thalach": 112,
    "exang": 1,
    "oldpeak": 1.2,
    "slope": 2,
    "ca": 1,
    "thal": 3
}
```

## Key Technologies Used
- **Machine Learning:** Scikit-Learn, Pandas, Numpy
- **Backend Development:** Flask, Gunicorn
- **Frontend Development:** HTML, CSS, JavaScript

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome!

---

Thank you for checking out this project! 😊
