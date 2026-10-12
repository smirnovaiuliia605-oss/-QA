import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = "https://ru.yougile.com/api-v2"
api_token = os.getenv("YOUGILE_API_TOKEN")

api_token = os.getenv("YOUGILE_API_TOKEN")

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}


def test_create_department():
    payload = {
        "title": "Подчинённый отдел №1",
        "parentId": "a09d726b-01b2-4769-96ed-02c058157547"
    }

    resp = requests.post(f"{base_url}/departments",
                         headers=headers, json=payload)

    assert resp.status_code == 201

    body = resp.json()
    assert "id" in body
    assert isinstance(body["id"], str)
    assert len(body["id"]) > 0
