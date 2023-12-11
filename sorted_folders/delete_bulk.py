import requests
import json

from elasticsearch import Elasticsearch


host="http://localhost:9200"



_requests=requests.Session()



def _request(op, *args, **kwargs):
        try:
            r=op(*args, **kwargs)
            if r.status_code==200 or r.status_code==201: 
                 return r.json()
            else:
                print("Request failed with status code: {}".format(r.status_code))
                print("Response content: {}".format(r.content))
            #print("Exception: {}".format(r.json()), flush=True)
        except Exception as e:
            print("Exception in request: {}".format(e), flush=True)
        raise Exception("error")



index_name='local_index'



def delete_bulk(bulk, batch=500, refresh="false"):
    ''' deletes bulk data from the database
        bulk: list of bulk data
    '''
    while bulk:
        cmds=[]
        for b in bulk[0:batch]:
            cmds.append({
                "delete":{
                    "_index":index_name,
                    #"_type":"_doc",  # ES6.8
                    "_id":b['_id']
                },
            })
            
            
        bulk = bulk[batch:]
            
        cmds="\n".join([json.dumps(x) for x in cmds])+"\n"
        print(cmds)
        _request(_requests.post,host+"/_bulk?refresh="+refresh,data=cmds,headers={"content-type":"application/x-ndjson"})

local_index = [
    {"_id": "1"},
    {"_id": "2"},
    {"_id": "3"},
    # Add more data to delete
]

# result=delete_bulk(index_name)
# print(result)

if isinstance(local_index, list):
    result = delete_bulk(local_index)  # Pass the local_index list as an argument
    print(result)
else:
    print("local_index is not a list of dictionaries.")


# result=delete_bulk(index_name)
# print(result)