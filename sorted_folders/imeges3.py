import requests
import json
import os

# Elasticsearch cluster ke URL
elasticsearch_url = 'https://192.168.111.156:31670/metadata_1d2_1d22/_search'

# Folder ka path jisme images hain
image_folder = '/home/aivid9/image999/'

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
response = requests.post(elasticsearch_url, data=json.dumps(search_query), headers=headers, verify=False, auth=(username, password))

# Response ko handle karein
if response.status_code == 200:
    results = response.json()
    for hit in results['hits']['hits']:
        source_data = hit['_source']
        image_path = source_data.get('path', 'N/A')
        license_plate = source_data.get('licensePlateNumber', 'N/A')
        
        # Extract image filename from the Elasticsearch path
        image_filename = os.path.basename(image_path)
        
        # Check if the image starts with 'img_' and exists in the specified folder
        if image_filename.startswith('rawImg_') and os.path.exists(os.path.join(image_folder, image_filename)):
            print(f'License Plate Number: {license_plate}, Image Path: {image_path}')
else:
    print(f"Error: {response.status_code}, {response.text}")
