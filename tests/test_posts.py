from starlette.testclient import TestClient

from app import app

client = TestClient(app)

def test_get_user_posts():
    # make a GET request to the endpoint with user_id=1
    response = client.get("/?user_id=1")
    assert response.status_code == 200
    # check that the response contains posts for user_id=1
    data = response.json()
    for post in data:
        assert post["user_id"] == 1