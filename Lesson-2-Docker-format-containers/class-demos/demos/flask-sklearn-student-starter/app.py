from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = f"<h3>Sklearn Prediction Home</h3>"
    return html.format(format)


@app.route("/predict")
def predict():
    html = f"<h3>prediction</h3>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
