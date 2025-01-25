from core.libs.exceptions import FyleError

def test_fyle_error_status_code():
    error = FyleError(status_code=401, message="Unauthorized")
    assert error.status_code == 401

def test_fyle_error_to_dict_with_status_code():
    error = FyleError(status_code=403, message="Forbidden")
    error_dict = error.to_dict()
    assert error_dict['message'] == "Forbidden"
    assert 'status_code' not in error_dict

def test_fyle_error_message():
    error = FyleError(status_code=400, message="Bad Request")
    assert error.message == "Bad Request"

def test_fyle_error_to_dict():
    error = FyleError(status_code=404, message="Not Found")
    error_dict = error.to_dict()
    assert error_dict['message'] == "Not Found"
