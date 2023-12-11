from elasticsearchmappinggenerator.elasticsearchmappinggenerator import ElasticMappingGenerator
import json
import sys
sys.path.append('/home/aivid9/Desktop/')


def main():
    _helper = ElasticMappingGenerator(number_of_replicas=1,number_of_shards=20)
    _helper.add_feilds(feild_name='first_name', type='text', index=True, keywords=False)
    _helper.add_feilds(feild_name='last_name', type='text', index=True)
    query = _helper.complete_mappings()
    print(json.dumps(query, indent=3))

if __name__ == '__main__':
    main()