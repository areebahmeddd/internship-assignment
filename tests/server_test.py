import pytest
from flask import Flask
from core.apis.responses import APIResponse

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app

def test_api_response(app):
    with app.app_context():
        response = APIResponse.respond(data={"message": "test"})
        assert response.status_code == 200
        assert response.json == {"data": {"message": "test"}}
