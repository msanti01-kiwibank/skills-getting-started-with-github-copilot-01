from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_signup_and_unregister_participant():
    activity_name = "Chess Club"
    email = "student@mergington.edu"

    # cleanup in case the test runs more than once in the same in-memory app
    client.delete(f"/activities/{activity_name}/signup?email={email}")

    signup_response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    assert signup_response.status_code == 200

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    assert email in activities_response.json()[activity_name]["participants"]

    unregister_response = client.delete(
        f"/activities/{activity_name}/signup?email={email}"
    )
    assert unregister_response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]
