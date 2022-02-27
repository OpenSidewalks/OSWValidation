from OSWValidation import validator

def test_validate_json_structure():
    assert validator.validate({}) == 1