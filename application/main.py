from flask import Flask, jsonify, request
from joblib import load
import pandas as pd

application = Flask(__name__)
model = load('application/model.joblib')


@application.route('/')
def index():
    return jsonify(result="Hello Elastic Beanstalk")


@application.route('/predict')
def predict():
    lookup = ('Setosa', 'Versicolor', 'Virginica')
    data = {
        'sepal_length': float(request.args.get('sepal_length')),
        'sepal_width': float(request.args.get('sepal_width')),
        'petal_length': float(request.args.get('petal_length')),
        'petal_width': float(request.args.get('petal_width')),
    }
    x = pd.DataFrame([data])
    y_pred, *_ = model.predict(x)
    y_prob, *_ = model.predict_proba(x)
    return {
        'Prediction': lookup[y_pred],
        'Confidence': f'{100 * max(y_prob):.2f}%',
    }
