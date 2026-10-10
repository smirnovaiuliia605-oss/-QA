import requests


base_url = "https://ru.yougile.com/api-v2/"
headers = {
    "Authorization": f"Bearer "
                     f"{'9Ui-NjuNlh-1Oq2O97kt8yB53BVNn42m0tTz4'
                        '+Zfr5XwAFufzsU8fQ-AC2JVZSkX'}"
}


def test_get_department():
    resp = requests.get(base_url+'/departments', headers=headers)
    body = resp.json()

    assert resp.status_code == 200
    assert len(body) > 0
