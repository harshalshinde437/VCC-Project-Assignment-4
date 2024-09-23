from django.shortcuts import render
import numpy as np
import joblib

# Load the saved model
model = joblib.load('fraud_detection_model.pkl')

def predict_fraud(request):
    fraud_prediction = None
    input_values = {}

    if request.method == 'POST':
        # Extract all the form data
        time = request.POST['Time']
        amount = request.POST['Amount']
        features = [request.POST[f'V{i}'] for i in range(1, 29)]

        # Store the input values to display them later in the table
        input_values['Time'] = time
        input_values['Amount'] = amount
        for i in range(1, 29):
            input_values[f'V{i}'] = request.POST[f'V{i}']

        # Prepare the input data for prediction
        input_data = np.array([time] + features + [amount], dtype=float).reshape(1, -1)

        # Make the prediction
        fraud_prediction = model.predict(input_data)[0]

    # Render the template and pass the prediction result and input values
    return render(request, 'predict.html', {
        'fraud_prediction': fraud_prediction,
        'input_values': input_values,
        'v_range': range(1, 29)  # Pass the range for V1 to V28
    })
