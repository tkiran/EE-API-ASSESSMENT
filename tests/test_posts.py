from starlette.testclient import TestClient
from controllers.Blog_Post_Controller import get_user_posts
import json

from app import app

client = TestClient(app)

def test_get_user_posts():
    # Set up authentication credentials
    auth = ('Kiran', 'Password')
    # Set up the client with basic authentication
    client.auth = auth
    # make a GET request to the endpoint with user_id=1
    response = client.get("/?user_id=1")
    assert response.status_code == 200
    # check that the response contains posts for user_id=1
    data = json.load(response)
    for post in data:
        assert post["user_id"] == 1

def test_get_user_posts_auth_negative():
    # Set up authentication credentials
    auth = ('Kiran1', 'Password')
    # Set up the client with basic authentication
    client.auth = auth
    # make a GET request to the endpoint with user_id=1
    response = client.get("/?user_id=5")
    assert response.status_code == 403

def test_get_user_posts_negative():
    # Set up authentication credentials
    auth = ('Kiran', 'Password')
    # Set up the client with basic authentication
    client.auth = auth
    # make a GET request to the endpoint with user_id=1
    response = client.get("/?user_id=5")

    # check that the response contains posts for user_id=1
    data = json.load(response)
    assert data == []