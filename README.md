## Heart Disease Prediction Model , Server And UI

### Overview

This project aims to build a machine learning model to predict heart disease using a dataset containing various medical attributes. create a flask server and UI for manage user request and predict the results. The project involves data preprocessing, model training, hyperparameter tuning, saving the final model using Python libraries such as `scikit-learn` and `pickle` create flask server, create and Ui .

### Dataset

The dataset used in this project contains the following features:

- **age**: Age of the patient (in years)
- **sex**: Sex of the patient (1 = male, 0 = female)
- **cp**: Chest pain type (1-4)
- **trestbps**: Resting blood pressure (in mm Hg on admission to the hospital)
- **chol**: Serum cholesterol in mg/dl
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- **restecg**: Resting electrocardiographic results (0-2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise-induced angina (1 = yes; 0 = no)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: The slope of the peak exercise ST segment
- **ca**: Number of major vessels (0-3) colored by fluoroscopy
- **thal**: Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)
- **target**: Presence or absence of heart disease (1 = yes, 0 = no)

### Steps Covered

1. **Data Loading and Preprocessing**
   - Handling missing values (if any).
   - Separating numerical and categorical features.
   - Applying standard scaling to numerical features.
   - Applying one-hot encoding to categorical features.

2. **Model Selection and Training**
   - Setting up a machine learning pipeline using `Pipeline` and `ColumnTransformer`.
   - Training models using `RandomForestClassifier`.
   - Hyperparameter tuning using `GridSearchCV`.

3. **Model Evaluation**
   - Evaluating the performance of the model using metrics like accuracy, confusion matrix, and classification report.

4. **Model Export**
   - Saving the best-performing model to a file using the `pickle` module.

5. **Model Loading and Prediction**
   - Loading the saved model and using it to make predictions on test data.

### Requirements

To run this notebook, you need the following Python libraries:

- `pandas`
- `scikit-learn`
- `numpy`
- `pickle`

You can install the necessary libraries using `pip`:

```bash
pip install pandas scikit-learn numpy
```

### How to Run

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NuwanSubasingha99/Heart-Disease-prediction.git
   ```

2. **Install Dependencies**

   Install the required Python libraries as mentioned above.

3. **Run the Jupyter Notebook**

   You can run the notebook using the following command:

   ```bash
   jupyter notebook Heart_Disease_Prediction.ipynb
   ```

4. **Save the Model**

   The notebook will guide you through training the model and saving it to a file.

5. **Load and Use the Model**

   The notebook also includes steps to load the saved model and use it for predictions on new data.

### Results

The model built in this project achieves a certain level of accuracy (depending on your dataset and hyperparameters). The specific performance metrics (e.g., accuracy, precision, recall) are included in the notebook.

### Conclusion

This project provides a comprehensive workflow for building, tuning, and deploying a machine learning model for heart disease prediction. It demonstrates the importance of data preprocessing, model selection, and hyperparameter tuning in achieving good predictive performance.

### License

### User Interface

![Screenshot 2024-08-06 160527](https://github.com/user-attachments/assets/0f7b16d2-873f-4070-bd79-502edfa467a7)


This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Thanks to the dataset provider for making the data available.
- Special thanks to the scikit-learn documentation and community for their invaluable resources.
