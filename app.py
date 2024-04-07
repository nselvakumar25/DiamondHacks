from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = 'AIzaSyCThWoDXD7um1H7EQE_-9pSBtzzJGUpG68'
BASE_URL = 'https://www.googleapis.com/civicinfo/v2'

@app.route('/api/elections', methods=['GET'])
def get_elections():
    # Constructing the request URL for Google Civic Information API
    url = f"{BASE_URL}/elections?key={API_KEY}"
    
    # Making the request to Google Civic Information API
    response = requests.get(url)
    if response.status_code == 200:
        # Forwarding the fetched data to the frontend
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data from Google Civic API'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5000)

