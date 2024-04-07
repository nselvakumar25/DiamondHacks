import requests

def fetch_civic_info(api_key, address):
    base_url = 'https://www.googleapis.com/civicinfo/v2'
    
    # GET /elections
    print("\nFetching Elections Information...")
    response = requests.get(f'{base_url}/elections', params={'key': api_key})
    print(response.json() if response.status_code == 200 else f"Error: {response.status_code}")
    
    # GET /voterinfo (Requires an electionId, using a placeholder here)
    print("\nFetching Voter Information...")
    election_id = '2000'  # Placeholder electionId
    response = requests.get(f'{base_url}/voterinfo', params={
        'address': address,
        'electionId': election_id,
        'key': api_key
    })
    print(response.json() if response.status_code == 200 else f"Error: {response.status_code}")
    
    # GET /representatives
    print("\nFetching Representatives Information...")
    response = requests.get(f'{base_url}/representatives', params={'address': address, 'key': api_key})
    print(response.json() if response.status_code == 200 else f"Error: {response.status_code}")
    
    # GET /representatives/ocdId (Requires an ocdId, using a placeholder here)
    print("\nFetching Specific Representative Information by ocdId...")
    ocd_id = 'ocd-division/country:us'  # Placeholder ocdId
    response = requests.get(f'{base_url}/representatives/{ocd_id}', params={'key': api_key})
    print(response.json() if response.status_code == 200 else f"Error: {response.status_code}")
    
    # GET /divisions (Requires a query, using 'New York' as an example)
    print("\nFetching Divisions Information...")
    query = 'New York'
    response = requests.get(f'{base_url}/divisions', params={'query': query, 'key': api_key})
    print(response.json() if response.status_code == 200 else f"Error: {response.status_code}")

# Example usage
api_key = 'AIzaSyCThWoDXD7um1H7EQE_-9pSBtzzJGUpG68' 
address = '8510 Costa Verde Blvd. 2208, CA, 92122'  # Example address
fetch_civic_info(api_key, address)
