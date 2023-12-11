from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime
import time


class Data:
    def __init__(self):#index_data
        es=Elasticsearch('http://localhost:9200')


        action=[
            {
                '_index':'aivid_index',
                #'_type':'doc',
                '_id':j,
                '_source':{
                    'any':"data" + str(j),
                    'timestamp': datetime.now()
                }
            }
            for j in range(1,101)
        ]

        st=time.time()
        helpers.bulk(es,action)
        end=time.time()
        print("total time",end-st)


        results=helpers.scan(es,index='aivid_index',query={'query':{'match_all':{}}})
        for item in results:
            print(item['_id'],item['_source'])


# if __name__ =='__main__':
#     index_data()
result=Data()
# result.index_data()