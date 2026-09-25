import pytest
def user_payload(uid=1, name="Damian", email="G00419511@atu.ie", age=21, student_id="G00419511"):
    return{"userid": uid, "name": name, "email": email, "age": age, "student_id": student_id}

def test_create_user_returns_201(client):
    response = client.post("api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["userid"] == 1
    assert data["name"] == "Damian"
    assert data["email"] == "G00419511@atu.ie"

def test_duplicate_user_id_returns_409(client):
    client.post("/api/users", json=user_payload(uid=2))

    response = client.post("/api/users", json=user_payload(uid=2))

    assert response.status_code == 409
    assert "exists" in response.json()["detail"].lower()

@pytest.mark.parametrize("bad_student_id", ["12345672", "g0043584", "G002", "G4091252"])

def test_bad_student_id_returns_422(client, bad_student_id):
    response = client.post("/api/users", json=user_payload(uid=3, student_id=bad_student_id))
    assert response.status_code == 422