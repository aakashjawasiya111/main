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
# document_id='1'

local_index = [
    {
        '_id': '1',
        '_doc': {
            'name': 'akash',
            'position': 'software engineer',
        },
    },
    {
        '_id': '2',
        '_doc': {
            'name': 'john',
            'position': 'data scientist',
        },
    },
    {
        '_id': '3',
        '_doc': {
            'name': 'sankalp sahu',
            'position': 'CV engineer',
        },
    },
    {
        '_id': '4',
        '_doc': {
            'name': 'mukund',
            'position': 'Python develeper',
        },
    },
     {
        '_id': '5',
        '_doc': {
            'name': 'vikash verma',
            'position': 'software engineer',
        },
    },
    {
        '_id': '6',
        '_doc': {
            'name': 'Devesh asawa',
            'position': 'JAVA developer',
        },
    },
    {
        '_id': '7',
        '_doc': {
            'name': 'param',
            'position': 'python intern',
        },
    },
    {
        '_id': '8',
        '_doc': {
            'name': 'Divya Saxena',
            'position': 'Tech-Team Leader',
        },
    },
]

print('################################ THIS IS A POST FUNCTION RESULT ##############################################')

def ingestBulkWithId(bulk, batch=500, refresh="false"):
    ''' save bulk data to the database
        bulk: list of bulk data [_id, _doc]
    '''
    while bulk:
        cmds=[]
        for b in bulk[0:batch]:
            cmds.append({
                "index":{
                    "_index":index_name,
                    #"_type":"_doc",  # ES6.8my_index
                    "_id" : b['_id']
                },
            })
            #print(cmds)
            cmds.append(b['_doc'])
            #print(cmds)
            
        bulk=bulk[batch:]
            
        cmds="\n".join([json.dumps(x) for x in cmds])+"\n"
        print(cmds)
        _request(_requests.post,host+"/_bulk?refresh="+refresh,data=cmds,headers={"content-type":"application/x-ndjson"})#_id=document_id


ingestBulkWithId(local_index)
# ingestBulkWithId(my_index, my_bulk_data)

print('################################# THIS IS A GET FUNCTION RESULT ##################################################')


def get(index_name,_id):
        return _request(_requests.get,host+"/"+index_name+"/_doc/"+_id,headers={'Content-Type':'application/json'})
result=get(index_name,_id='8')
print(result)

print('################################ To Chech Health Of The Cluster ###################################################')


def health():
    r=_request(_requests.get,host+"/_cluster/health")
    return r["status"]=="green" or r["status"]=="yellow"

result1=health()
print(result1)