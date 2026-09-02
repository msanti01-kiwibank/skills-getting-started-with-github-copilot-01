from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_signup_and_unregister_participant():
    # Arrange
    activity_name = "Chess Club"
    email = "student@mergington.edu"
    client.delete(f"/activities/{activity_name}/signup?email={email}")

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    activities_after_signup = client.get("/activities")
    unregister_response = client.delete(
        f"/activities/{activity_name}/signup?email={email}"
    )
    activities_after_unregister = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    assert activities_after_signup.status_code == 200
    assert email in activities_after_signup.json()[activity_name]["participants"]
    assert unregister_response.status_code == 200
    assert email not in activities_after_unregister.json()[activity_name]["participants"]
