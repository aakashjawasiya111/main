import requests
import json
#from language_dsl import text
from elasticsearch import Elasticsearch


host="http://localhost:9200"



_requests=requests.Session()

def _requests(op, *args, **kwargs):
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


index_name='my_index'

my_index=[
        {
            'name':'akash',
            'position':'software engineer',

        },
        {
            'name':'sankalp',
            'position':'Cv engineer'
        },
        {
            'name':'mukund',
            'position':'python developer'
        },
        {
            'name':'kanil patel',
            'position':'CV engineer'
        }
]




def ingest_bulk(bulk, batch=500, refresh="false"):
    ''' save bulk data to the database
        bulk: list of bulk data
    '''
    while bulk:
        cmds=[]
        for b in bulk[0:batch]:
            cmds.append({
                "index":{
                    "_index":index_name,
                    # "_type":"_doc",  # ES6.8
                },
            })
            print(cmds)
            cmds.append(b)
            print(cmds)
        bulk=bulk[batch:]
            
        cmds="\n".join([json.dumps(x) for x in cmds])+"\n"
        print(cmds)

        _request(_requests.post,host+"/_bulk?refresh="+refresh,data=cmds,headers={"content-type":"application/x-ndjson"})

# result_1=es.get(index="python-elastic",body=doc,id=D_id)
# print(result_1)


ingest_bulk(my_index)




# def _request(op, *args, **kwargs):
#     try:
#         r = op(*args, **kwargs)
#         if r.status_code == 200 or r.status_code == 201:
#             return r.json()
#         else:
#             print("Request failed with status code: {}".format(r.status_code))
#             print("Response content: {}".format(r.content))
#     except Exception as e:
#         print("Exception in request: {}".format(e), flush=True)
#     raise Exception("Error occurred during the request.")
