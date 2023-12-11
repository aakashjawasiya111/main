import json
import requests
import urllib3

# Disable SSL certificate verification (not recommended for production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    scheme = "https"
    hostname = "192.168.111.156"  # Update with your Elasticsearch server's hostname or IP address
    port = "31670"               # Update with your Elasticsearch server's port if different

    # Construct the host_url
    host_url = f"{scheme}://{hostname}:{port}"
    print('Connection success')
except Exception as e:
    print('Connection failed: {}'.format(e))

# Create a requests session
_requests = requests.Session()

username = "elastic"  # Replace with your Elasticsearch username
password = "admin"  # Replace with your Elasticsearch password

def _request(op, *args, **kwargs):
    try:

        auth = HTTPBasicAuth(username, password)

        r = op(*args,auth=auth, **kwargs)
        if r.status_code == 200 or r.status_code == 201:
            return r.json()
        else:
            print("Request failed with status code: {}".format(r.status_code))
            print("Response content: {}".format(r.content))
    except Exception as e:
        print("Exception in request: {}".format(e))
    raise Exception("error")

index_name = 'metadata_1d2_1d22'
document_type = "_doc"

# Construct the request_url
request_url = f"{host_url}/{index_name}/{document_type}"

print("host_url:", host_url)
print("request_url:", request_url)

def get(index_name):
    return _request(_requests.post, request_url, headers={'Content-Type': 'application/json'}, verify=False)

result = get(index_name)
print(result)
