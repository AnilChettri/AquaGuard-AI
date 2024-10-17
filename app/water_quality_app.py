# app/water_quality_app.py
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load('model/water_quality_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        pH = float(request.form['pH'])
        temperature = float(request.form['temperature'])
        turbidity = float(request.form['turbidity'])

        # Prediction
        prediction = model.predict([[pH, temperature, turbidity]])[0]
        result = 'Contaminated' if prediction == 1 else 'Clean'

        return render_template('result.html', pH=pH, temperature=temperature, turbidity=turbidity, result=result)

if __name__ == '__main__':
    app.run(debug=True)
