"""
API Operations
This module demonstrates how to work with APIs in Python for data engineering.
"""

import requests
import json
import pandas as pd
from datetime import datetime
import time

class APIClient:
    """A class to handle API operations"""
    
    def __init__(self, base_url, api_key=None):
        """Initialize the API client"""
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def get(self, endpoint, params=None):
        """Make a GET request"""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making GET request: {e}")
            return None
    
    def post(self, endpoint, data):
        """Make a POST request"""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making POST request: {e}")
            return None

def fetch_weather_data(city, api_key):
    """Fetch weather data from OpenWeatherMap API"""
    base_url = "http://api.openweathermap.org/data/2.5"
    client = APIClient(base_url)
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    return client.get('weather', params=params)

def fetch_stock_data(symbol, api_key):
    """Fetch stock data from Alpha Vantage API"""
    base_url = "https://www.alphavantage.co/query"
    client = APIClient(base_url)
    
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key
    }
    
    return client.get('', params=params)

def process_stock_data(data):
    """Process stock data into a pandas DataFrame"""
    if not data or 'Time Series (Daily)' not in data:
        return None
    
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df.index = pd.to_datetime(df.index)
    
    # Rename columns
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    
    # Convert string values to float
    for col in df.columns:
        df[col] = df[col].astype(float)
    
    return df

def fetch_and_save_data():
    """Demonstrate fetching and saving data from multiple APIs"""
    # Example API keys (replace with your actual API keys)
    weather_api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    stock_api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
    
    # Fetch weather data
    weather_data = fetch_weather_data("London", weather_api_key)
    if weather_data:
        print("\nWeather Data:")
        print(json.dumps(weather_data, indent=2))
        
        # Save weather data
        with open('weather_data.json', 'w') as f:
            json.dump(weather_data, f, indent=2)
    
    # Fetch stock data
    stock_data = fetch_stock_data("AAPL", stock_api_key)
    if stock_data:
        # Process stock data
        df = process_stock_data(stock_data)
        if df is not None:
            print("\nStock Data (first 5 rows):")
            print(df.head())
            
            # Save stock data
            df.to_csv('stock_data.csv')
    
    # Demonstrate rate limiting
    print("\nDemonstrating rate limiting...")
    for i in range(3):
        print(f"Request {i+1}")
        time.sleep(1)  # Wait 1 second between requests

def create_mock_api():
    """Create a simple mock API using Flask"""
    from flask import Flask, jsonify, request
    
    app = Flask(__name__)
    
    # Sample data
    users = [
        {'id': 1, 'name': 'John', 'age': 30},
        {'id': 2, 'name': 'Anna', 'age': 25}
    ]
    
    @app.route('/users', methods=['GET'])
    def get_users():
        return jsonify(users)
    
    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        new_user = {
            'id': len(users) + 1,
            'name': data['name'],
            'age': data['age']
        }
        users.append(new_user)
        return jsonify(new_user), 201
    
    return app

if __name__ == "__main__":
    # Demonstrate API operations
    print("=== API Operations Demo ===")
    
    # Fetch and save data
    fetch_and_save_data()
    
    # Create and run mock API
    app = create_mock_api()
    print("\nMock API created. You can test it using:")
    print("GET http://localhost:5000/users")
    print("POST http://localhost:5000/users with JSON body: {'name': 'New User', 'age': 28}")
    
    # Uncomment the following line to run the mock API
    # app.run(debug=True) 