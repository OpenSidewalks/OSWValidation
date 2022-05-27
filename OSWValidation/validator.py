import os, json
from . import json_structure

def validate_with_schema(geojson, schema_path):
    with open(os.path.abspath(schema_path), 'r') as fp:
        schema = json.load(fp)
    return json_structure.validate_json_structure_with_schema(geojson, schema)

def validate(geojson):
    invalid_schema_ways_dict = json_structure.validate_json_structure(geojson)
    return invalid_schema_ways_dict