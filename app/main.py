from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('heart_disease_rf_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Parse JSON input
    input_data = request.json
    features = np.array(input_data['features']).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)
    probability = model.predict_proba(features)
    
    # Respond with prediction and probability
    return jsonify({
        'prediction': int(prediction[0]),
        'probability': probability.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)
