from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = 'AIzaSyCThWoDXD7um1H7EQE_-9pSBtzzJGUpG68'
BASE_URL = 'https://www.googleapis.com/civicinfo/v2'

@app.route('/api/elections')
def fetch_elections():
    response = requests.get(f'{BASE_URL}/elections', params={'key': API_KEY})
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
