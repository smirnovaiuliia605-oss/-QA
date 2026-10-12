import requests

base_url = "https://ru.yougile.com/api-v2"


def test_auth_without_body_negative():
    headers = {
        "Content-Type": "application/json"
    }

    resp = requests.post(f"{base_url}/auth/keys/get", headers=headers)

    assert resp.status_code == 400

    body = resp.json()
    assert "error" in body or "message" in body
