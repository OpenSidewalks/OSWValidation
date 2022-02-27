import os
import sys
import json
from OSWValidation import validator

def test_validate_entire_dataset():
    test_dataset_filename = 'tests/TestData/valparaiso/input/valparaiso_ways.geojson'

    with open(os.path.join(sys.path[0], test_dataset_filename), 'r') as fp:
        geojson = json.load(fp)
    assert validator.validate(geojson) == 1