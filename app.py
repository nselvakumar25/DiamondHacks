from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/elections', methods=['GET'])
def get_elections():
    api_key = request.args.get('api_key')
    base_url = 'https://www.googleapis.com/civicinfo/v2/elections'
    response = requests.get(base_url, params={'key': api_key})
    return jsonify(response.json()) if response.status_code == 200 else jsonify({"error": response.status_code}), response.status_code

@app.route('/api/voterinfo', methods=['GET'])
def get_voter_info():
    api_key = request.args.get('api_key')
    address = request.args.get('address')
    election_id = request.args.get('electionId', '2000')  # Defaulting to '2000' if not provided
    base_url = 'https://www.googleapis.com/civicinfo/v2/voterinfo'
    response = requests.get(base_url, params={'address': address, 'electionId': election_id, 'key': api_key})
    return jsonify(response.json()) if response.status_code == 200 else jsonify({"error": response.status_code}), response.status_code

# Define additional routes for '/representatives' and '/divisions' similarly

if __name__ == '__main__':
    app.run(debug=True)
