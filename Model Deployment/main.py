
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Create Flask App
app = Flask(__name__)


# Connect POST API Call ---> predict() Function
# #http://localhost:5000/predict
@app.route('/predict', methods=['POST'])
def predict():

    # Get Json request
    feat_data = request.json
    # Convert Json to Pandas df (col names)
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)
    # Predict
    prediction = list(model.predict(df))

    return jsonify({'prediction':str(prediction)})


# Load my model and load column names
if __name__ == '__main__':

    model = joblib.load('final_model.pkl')
    col_names = joblib.load('column_names.pkl')

    app.run(debug=True)













