from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Welcome to My Flask Application!"



def test_contact():
    client = app.test_client()

    response = client.get("/contact")

    assert response.status_code == 200
    assert response.data == b"Contact page of my Flask application."