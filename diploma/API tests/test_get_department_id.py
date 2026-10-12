import os
import requests


base_url = "https://ru.yougile.com/api-v2"
api_token = os.getenv("YOUGILE_API_TOKEN")

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}


def test_get_department_by_id():
    department_id = "0ca3766d-e03d-4361-ac1f-91e0d9134d4b"

    resp = requests.get(f"{base_url}/departments/{department_id}",
                        headers=headers)

    assert resp.status_code == 200
