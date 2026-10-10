import requests

# Базовый URL YouGile API v2 (слэш на конце не ставим!)
base_url = "https://ru.yougile.com/api-v2/"

headers = {
    "Authorization": f"Bearer {'9Ui-NjuNlh-1Oq2O97kt8yB53BVNn42m0tTz4'
                               '+Zfr5XwAFufzsU8fQ-AC2JVZSkX'}",
    "Content-Type": "application/json"
}


def test_create_department():
    # Тело запроса в формате JSON
    payload = {
        "title": "Подчинённый отдел №1",
        "parentId": "a09d726b-01b2-4769-96ed-02c058157547"
    }

    # Выполняем POST-запрос.
    resp = requests.post(base_url + '/departments',
                         headers=headers, json=payload)

    assert resp.status_code == 201

    body = resp.json()
    assert "id" in body
    assert isinstance(body["id"], str)
    assert len(body["id"]) > 0
