from OSWValidation import json_structure

def test_emptyFeatures_pass():
    features = []
    invalid_ids = json_structure.validate_json_structure(features)
    assert len(invalid_ids) == 0

"""
CROSSINGS
"""

def test_crossing_valid_pass():
    features = [{
        "type": "Feature",
        "properties": {
            "highway": "footway",
            "footway": "crossing",
            "crossing": "marked",
            "_u_id": "364328711",
            "_v_id": "4561052271"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [ -71.6266856, -33.0416369 ],
                [ -71.6266685, -33.0416575 ]
            ]
        }
    }]
    geojson = generate_geojson_from_features(features)
    invalid_ids = json_structure.validate_json_structure(geojson)
    assert len(invalid_ids) == 0

def test_crossing_old_schema_fail():
    features = [{
        "type": "Feature",
        "properties": {
            "highway": "footway",
            "width": None,
            "footway": "crossing",
            "crossing": "unmarked",
            "length": 2.8
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [ -71.6266856, -33.0416369 ],
                [ -71.6266685, -33.0416575 ]
            ]
        }
    }]
    geojson = generate_geojson_from_features(features)
    invalid_ids = json_structure.validate_json_structure(geojson)
    assert len(invalid_ids) != 0

def test_crossing_invalid_fail():
    features = [{
        "type": "Feature",
        "properties": {
            "highway": "footway",
            "width": 10,
            "footway": "crossing",
            "crossing": "unmarked",
            "length": 2.8
        },
        "gometry": {
            "type": "LineString",
            "coordinates": [
                [ -71.6266856, -33.0416369 ],
                [ -71.6266685, -33.0416575 ]
            ]
        }
    }]
    geojson = generate_geojson_from_features(features)
    invalid_ids = json_structure.validate_json_structure(geojson)
    assert len(invalid_ids) == 1

"""
SIDEWALKS
"""
def test_sidewalk_valid_pass():
    features = [{
        "type": "Feature",
        "properties": {
            "highway": "footway",
            "footway": "sidewalk",
            "_u_id": "364328711",
            "_v_id": "4561052271"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [ -71.6266856, -33.0416369 ],
                [ -71.6266685, -33.0416575 ]
            ]
        }
    }]
    geojson = generate_geojson_from_features(features)
    invalid_ids = json_structure.validate_json_structure(geojson)
    assert len(invalid_ids) == 0

def test_sidewalk_missing_vid_uid_fail():
    features = [{
        "type": "Feature",
        "properties": {
            "highway": "footway",
            "footway": "sidewalk",
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [ -71.6266856, -33.0416369 ],
                [ -71.6266685, -33.0416575 ]
            ]
        }
    }]
    geojson = generate_geojson_from_features(features)
    invalid_ids = json_structure.validate_json_structure(geojson)
    assert len(invalid_ids) != 0

"""
Helper functions:
"""
def generate_geojson_from_features(features):
    return {
        "type": "FeatureCollection",
        "features": features
    }