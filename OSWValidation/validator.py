import os
import sys
import json
from . import json_structure

def validate(geojson):
    print(os.getcwd())
    with open(os.path.join(sys.path[0], 'OSWValidation/Json Schema/Ways_schema.json'), 'r') as fp:
        schema = json.load(fp)

    invalid_schema_ways_dict = json_structure.validate_json_structure(geojson, schema)
    return 1