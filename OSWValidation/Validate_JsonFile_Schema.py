from config import DefaultConfigs
import json
from json_structure import validate_json_structure

def validate_json_schema(geojson_path=None, schema_path=None, writePath=None):
    # Read schema and json files

    with open(geojson_path) as fp:
        geojson = json.load(fp)
    with open(schema_path) as fp:
        schema = json.load(fp)

    return validate_json_structure(geojson, schema)


if __name__ == '__main__':
    cf = DefaultConfigs()
