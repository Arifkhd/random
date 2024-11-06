# app/views.py
from flask import Blueprint, render_template, request, jsonify
import pickle
import numpy as np

# Define the blueprint
app = Blueprint('app', __name__)

# Load the pre-trained model
with open('app/iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        
        # Make a prediction
        prediction = model.predict(np.array([[sepal_length, sepal_width, petal_length, petal_width]]))
        species = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
        result = species[prediction[0]]
        
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})
