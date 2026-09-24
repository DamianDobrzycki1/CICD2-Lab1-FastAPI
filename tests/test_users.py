def user_payload(uid=1, name="Damian", email="G00419511@atu.ie", age=21, student_id="G00419511"):
    return {"userid" : uid, "name": name, "email": email, "age": age, "student_id": student_id}

def test_create_user_returns_201(client):
    response = client.post("api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["userid"] == 1
    assert data["name"] == "Damian"
    assert data["email"] == "G00419511@atu.ie"