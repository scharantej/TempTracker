
# main.py

from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime

# Load historical temperature data
df = pd.read_csv('temperature_data.csv')

# Create Flask application
app = Flask(__name__)

# Main page route
@app.route('/')
def index():
    return render_template('index.html')

# Details page route
@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'GET':
        location = request.args.get('location')
        data = get_location_data(location)
        return render_template('details.html', data=data)
    elif request.method == 'POST':
        location = request.form.get('location')
        return redirect(url_for('details', location=location))

# Historical data route
@app.route('/data/<date>')
def get_historical_data(date):
    data = df[df['Date'] == date]
    return jsonify(data.to_dict('records'))

# Average data route
@app.route('/average-data/<location>')
def get_average_data(location):
    data = df[df['Location'] == location]
    return jsonify(data.groupby('Date')['Temperature'].mean().to_dict())

# Forecast data route
@app.route('/forecast-data/<location>')
def get_forecast_data(location):
    # Placeholder data for demonstration
    data = {'Temperature': np.random.randint(30, 100, 7)}
    return jsonify(data)

# Helper function to get location data
def get_location_data(location):
    data = df[df['Location'] == location]
    return data.to_dict('records')[0]

if __name__ == '__main__':
    app.run(debug=True)
