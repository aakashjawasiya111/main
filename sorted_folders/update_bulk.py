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
    # {
    #     '_id': '4',
    #     '_doc': {
    #         'name': 'mukund',
    #         'position': 'Python develeper',
    #     },
    # },
    #  {
    #     '_id': '5',
    #     '_doc': {
    #         'name': 'vikash verma',
    #         'position': 'software engineer',
    #     },
    # },
    # {
    #     '_id': '6',
    #     '_doc': {
    #         'name': 'Devesh asawa',
    #         'position': 'JAVA developer',
    #     },
    # },
    # {
    #     '_id': '7',
    #     '_doc': {
    #         'name': 'param',
    #         'position': 'python intern',
    #     },
    # },
    # {
    #     '_id': '8',
    #     '_doc': {
    #         'name': 'Divya Saxena',
    #         'position': 'Tech-Team Leader',
    #     },Request failed with status code: 400
]






def update_bulk(updates, batch=500):
    """ update in a bulk:
        updates: list of [_id, _doc]
    """
    while updates:
        cmds=[]
        for u in updates[0:batch]:
            cmds.append({ "update": {
                "_index":index_name,
                #"_type":"_doc", #ES6.8
                "_id": u['_id']
            }})
            cmds.append({ "doc": u['_doc'],"doc_as_upsert" : True})
        updates=updates[batch:]

        cmds="\n".join([json.dumps(x) for x in cmds])+"\n"
        print(cmds)
        _request(requests.post,host+"/_bulk",data=cmds,headers={"content-type":"application/x-ndjson"})


result=update_bulk(local_index)
print(result)
