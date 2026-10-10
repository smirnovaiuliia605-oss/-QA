import requests

# Базовый URL YouGile API v2
base_url = "https://ru.yougile.com/api-v2/"

headers = {
    "Authorization": f"Bearer {'9Ui-NjuNlh-1Oq2O97kt8yB53BVNn42m0tTz4'
                               '+Zfr5XwAFufzsU8fQ-AC2JVZSkX'}",
    "Content-Type": "application/json"
}

headers = {
    "Authorization": f"Bearer {'9Ui-NjuNlh-1Oq2O97kt8yB53BVNn42m0tTz4'
                               '+Zfr5XwAFufzsU8fQ-AC2JVZSkX'}",
    "Content-Type": "application/json"
}


def test_create_department_negative():
    # Намеренно не указываем обязательное поле "title"
    payload = {
        "parentId": "a09d726b-01b2-4769-96ed-02c058157547"
    }

    # Отправляем POST-запрос на создание отдела в контексте компании
    resp = requests.post(f"{base_url}/departments",
                         headers=headers, json=payload)

    # 2. Проверяем ожидаемый негативный статус-код 400 Bad Request
    assert resp.status_code == 400
