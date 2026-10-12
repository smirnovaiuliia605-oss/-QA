import os
import requests


base_url = "https://ru.yougile.com/api-v2/"
api_token = os.getenv("YOUGILE_API_TOKEN")
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}


def test_get_department():
    resp = requests.get(base_url+'/departments', headers=headers)
    body = resp.json()

    assert resp.status_code == 200
    assert len(body) > 0
