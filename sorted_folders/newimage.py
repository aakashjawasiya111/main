import os
import re
from elasticsearch import Elasticsearch
import requests

# try:
#     response = requests.get('https://192.168.111.156:31670')
#     print('success')
# except error as e:
#     print('faild',{}.format(e))


# ElasticSearch host aur port ki details
try:
    # es_host = 'https://192.168.111.156:31670'
    # es_port = 31670
    # es_scheme = 'https'
    host = [{'host': '192.168.111.156', 'port': 9200, 'scheme': 'https'}]
    IS_SSL = str(["IS_SSL"])
    if IS_SSL == "true":
            requests.cert = ("/home/ssl/bundle.crt", "/home/ssl/private.key")
            requests.verify =  False
    # es = Elasticsearch([{'host': es_host, 'port': es_host , 'scheme': es_scheme}])
    print('conection success')
except error as e:
    print('connection faild',{}.format(e))


# Folder path jahan se images ko scan karna hai
image_folder = '/home/aivid9/image999'

# ElasticSearch index jahan data store hua hai
index_name = 'metadata_1d2_1d22'

# Target folder jahan renamed images ko save karna hai
target_folder = '/home/aivid9/getimages'

# Function jo ElasticSearch me query karega aur image names ko update karega
# Function to query Elasticsearch and update image names


def request(method, url, **kwargs):
    pass
    # try:
    #     response = method(url, **kwargs)
    #     response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx status codes)
    #     return response
    # except requests.exceptions.RequestException as e:
    #     print(f"Request failed: {str(e)}")
    #     return None

# Now you can use the _request function in your code
# response = request(requests.get, 'https://192.168.111.156:31670')
# if response:
#     print(response.text)
_index = "metadata_1d2_1d22"# return request(requests.get,host+"/"+_index+"/metadata_1d2_1d22/"+_source,headers={'Content-Type':'application/json'})

try:
    def get(_index):
        _index = "metadata_1d2_1d22"# return request(requests.get,host+"/"+_index+"/metadata_1d2_1d22/"+_source,headers={'Content-Type':'application/json'})
except error as e :
    print(f"get function not work{e}")



get(_index)
try:
    def process_images_and_update_names():
        try:
            es = Elasticsearch(hosts=host) #{host: es_host, port: es_host, scheme: es_scheme}

            pattern = re.compile(r'rawImg_(\d+)_')
            try:
                for root, _, files in os.walk(image_folder):
                    for file in files:
                        image_path = os.path.join(root, file)
                        print('loop success')
                        
                        # Extract numeric part from file name using regex
                        match = pattern.search(file)
                        if match:
                            image_number_str = match.group(1)
                            image_number = (image_number_str)
                        else:
                            print(f"Invalid file name format for file: {file}")
                            continue
                        
                        # Elasticsearch query
                    
                        query = {
                            "query": {
                                "bool": {
                                    "must": [
                                        {
                                            "match": {
                                                "licensePlateNumber": {
                                                    "query": f"{image_number}",
                                                    "boost": 1.0
                                                }
                                            }
                                        },
                                        {
                                            "term": {
                                                "path.keyword": f"/{image_number}.jpeg"
                                            }
                                        }
                                    ]
                                }
                            }
                        }

                    
                        
                        # Query Elasticsearch
                        result = es.search(index=index_name, body=query)
                        hits = result['hits']['hits']
                        
                        if hits:
                            # Data retrieved from Elasticsearch
                            elastic_data = hits[0]['_source']
                            
                            # Extract LicensePlateNumber and update image name
                            new_image_name = f"{elastic_data['licensePlateNumber']}.jpg"
                            new_image_path = os.path.join(target_folder, new_image_name)
                            
                            # Rename the image
                            os.rename(image_path, new_image_path)
                            print(f"Image '{file}' renamed to '{new_image_name}'.")
                        else:
                            print(f"No data found in Elasticsearch for image '{file}'.")
            except Exception as e:
                print('loop not working',{}.format(e))

        except Exception as e:
            print('Exception:', str(e))

except error as e :
    print('function work',{}.format(e))


try:
    process_images_and_update_names()
except Exception as e:
    print(f'Exception:{e}')