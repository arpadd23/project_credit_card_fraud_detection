from flask import Flask, request, render_template
import joblib
import numpy as np
import os
# Load your trained model
model = joblib.load('credit_card_model.pkl')  # Ensure the model file path is correct

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve form data
        feature_values = []
        for i in range(1, 30):
            feature = request.form.get(f'V{i}', type=float)
            feature_values.append(feature)
        feature_values = np.array([feature_values])

        # Make prediction
        prediction = model.predict(feature_values)
        result = 'Fraudulent Transaction' if prediction[0] == 1 else 'Normal Transaction'
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True, port=5100)
