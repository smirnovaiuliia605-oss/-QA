import requests

# Базовый URL (без лишнего слэша на конце для безопасной склейки)
base_url = "https://ru.yougile.com/api-v2"

headers = {
    "Authorization": f"Bearer {'9Ui-NjuNlh-1Oq2O97kt8yB53BVNn42m0tTz4'
                               '+Zfr5XwAFufzsU8fQ-AC2JVZSkX'}",
    "Content-Type": "application/json"
}


def test_get_department_by_id():
    # 1. Задаем ID существующего отдела, который мы хотим проверить
    department_id = "0ca3766d-e03d-4361-ac1f-91e0d9134d4b"

    # 2. Выполняем GET-запрос
    resp = requests.get(f"{base_url}/departments/{department_id}",
                        headers=headers)

    # 3. Проверяем, что сервер вернул успешный статус-код 200 OK
    assert resp.status_code == 200
