import requests
from elasticsearch_dsl import Search
from dsl_lex import lexer

requests_session = requests.Session()
requests_session.auth= ("elastic","admin")
requests_session.verify= False

class MyElasticsearchClient:
    def __init__(self, host, index):
        self._host = host
        self._index = index

    def get_spec(p, var):
        return p.parser.specs

    def _spec_from_index(self):
        spec = {"nested": [], "types": {}}
        r = self._make_request(requests_session.get, self._host + "/" + self._index + "/_mapping", params={"include_type_name": "true"})
        for index1 in r:
            self._spec_from_mapping(spec, "", r[index1]["mappings"]["properties"])
        return spec

    def _make_request(self, op, *args, **kwargs):
        try:
            r = op(*args, **kwargs)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to make the request: {e}")
            raise Exception("Error in request")

    def compile(self,queries,specs={}):
        parser.specs = specs
        dsl = parser.parse(queries, lexer=lexer)
        if dsl is None: dsl = {"match_none":{}}
        return dsl

    def search(self, queries, size=10000, spec=None):
        if spec is None:
            spec = self._spec_from_index()

        dsl = self.compile(queries, spec)

        url = f"{self._host}/{self._index}/_search"
        request_data = {
            "query": dsl,
            "size": size,
            "seq_no_primary_term": True
        }

        r = self._make_request(requests_session.post, url, json=request_data)

        for x in r["hits"]["hits"]:
            yield x

# Usage example
if __name__ == "__main__":
    es_client = MyElasticsearchClient("https://192.168.111.151:31449", "akash_tensors_23d0368587_72d6505842")
    queries = [
        # Define your queries here
    ]

    results = es_client.search(queries, size=1000)
    for result in results:
        # Process each result as needed
        print(result)
