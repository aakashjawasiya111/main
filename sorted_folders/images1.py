import requests
import json

# Elasticsearch cluster ke URL
url = 'https://192.168.111.156:31670/metadata_1d2_1d22/_search'

# Authentication credentials
username = 'elastic'
password = 'admin'

# Elasticsearch search query
search_query = {
    "query": {
        "match_all": {}  # Sabhi documents ko retrieve karne ke liye
    }
}

# Content-Type header ko set karein
headers = {
    'Content-Type': 'application/json',
    'compatible-with': '8'  # Aapke Elasticsearch version ke hisab se
}

# Elasticsearch par POST request bhejen
response = requests.post(url, data=json.dumps(search_query), headers=headers, verify=False, auth=(username, password))

# Response ko handle karein
if response.status_code == 200:
    results = response.json()
    for hit in results['hits']['hits']:
        source_data = hit['_source']
        license_plate = source_data.get('licensePlateNumber', 'N/A')
        image_path = source_data.get('path', 'N/A')
        print(f'License Plate Number: {license_plate}, Image Path: {image_path}')
else:
    print(f"Error: {response.status_code}, {response.text}")
