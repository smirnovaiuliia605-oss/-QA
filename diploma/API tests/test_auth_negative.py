import requests

# Базовый URL согласно вашему условию
base_url = "https://ru.yougile.com/api-v2"


def test_auth_without_body_negative():
    # Намеренно НЕ передаем payload (тело запроса)
    headers = {
        "Content-Type": "application/json"
    }

    # Выполняем POST-запрос на эндпоинт получения ключей без тела
    resp = requests.post(f"{base_url}/auth/keys/get", headers=headers)

    # 1. Проверяем ожидаемый негативный статус-код 400 Bad Request
    assert resp.status_code == 400

    # 2. Проверяем, что сервер вернул ошибку в формате JSON
    body = resp.json()
    assert "error" in body or "message" in body
