from fastapi.testclient import TestClient
import json

from index import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

    reply = {"message": "Hello from Fastapi, we are cooking now!"}
    assert response.json() == reply


def test_post_tsne():

    f = open("api/demo_embedding.txt", "r")
    data_as_string = f.read()

    response = client.post(
        "/tsne",
        headers={"X-Token": "coneofsilence"},
        json={"data": data_as_string},

    )
    assert response.status_code == 200

    returned_list = response.json()

    assert len(returned_list) == 2
    assert type(returned_list) == list
