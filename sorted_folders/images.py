import requests
import json, os

# Elasticsearch cluster ke URL
url = 'https://192.168.111.10:31557/metadata_22d3091842_73d1703512/_search' #metadata_1d2_1d22

# Authentication credentials
username = 'elastic'
password = 'admin'

bot_config_id = "650443f128cac400652277f6"         #'6502ee4fb77e5f00651c6fa6'
# Elasticsearch search query
search_query = {
    "query": {
        "term": {
            "botConfigId": bot_config_id
        }
    },
    "size": 10000
}

# Content-Type header ko set karein
headers = {
    'Content-Type': 'application/json',
    'compatible-with': '8'  # Aapke Elasticsearch version ke hisab se
}

# Elasticsearch par POST request bhejen
response = requests.post(url, data=json.dumps(search_query), headers=headers, verify=False,  auth=(username, password))

# Response ko handle karein
img_PATH = "/opt/aivid-storage-disk-0/aividsetup/worker/aividpv/office-storage-image/site-master"
if response.status_code == 200:
    results = response.json()
    for hit in results['hits']['hits']:
        source_data = hit['_source']
        # print(source_data)
        if "path" in source_data and "licensePlateNumber" in source_data:
            raw_path = img_PATH+source_data["path"].replace("img","rawImg")
            if os.path.exists(raw_path):
                new_path = f"/home/aivid9/Desktop/{bot_config_id}"
                os.makedirs(new_path, exist_ok=True)
                new_path = new_path+f"/{source_data['licensePlateNumber']}.jpeg"
                os.system(f"cp {raw_path}  {new_path}")
else:
    print(f"Error: {response.status_code}, {response.text}")
