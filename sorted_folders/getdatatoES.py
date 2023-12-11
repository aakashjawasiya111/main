import requests

# Define your query
query = {
    "query": {
        "term": {
            "licensePlateNumber": "RJ0168B171"
        }
    }
}

# Send the query to Elasticsearch
response = requests.get("https://https://192.168.111.156:31670/metadata_1d2_1d22/_doc/_search", json=query)

# Parse the JSON response
data = response.json()

# Extract and process the retrieved documents from the 'hits' field
hits = data["hits"]["hits"]
for hit in hits:
    # Process the retrieved document
    document = hit["_source"]
    print(document)
