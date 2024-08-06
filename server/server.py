from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import utill


app = Flask(__name__, template_folder='ui', static_folder='ui/static')

# Load the trained model
with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from JSON payload
        data = request.get_json()
        print(data)
        # Ensure all required fields are present
        required_fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing fields in request data.'})
        
        correct_data = utill.convert_to_correct_types(data)
        
        # Convert to DataFrame
        input_df = pd.DataFrame([correct_data])

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Return the result as JSON
        return jsonify({'prediction': 'likely' if prediction == 1 else 'not likely'})

    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred: ' + str(e)})

if __name__ == '__main__':
    app.run(debug=True)
