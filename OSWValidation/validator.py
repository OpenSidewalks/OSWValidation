from . import json_structure

def validate(geojson):
    invalid_schema_ways_dict = json_structure.validate_json_structure(geojson)
    return invalid_schema_ways_dict