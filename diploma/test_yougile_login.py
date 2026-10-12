import allure
from selenium.webdriver.common.by import By


@allure.epic("Авторизация")
@allure.feature("Вход в систему")
@allure.story("Успешная авторизация и проверка имени пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_yougile_login(authorized_driver):

    with allure.step("Переход в настройки аккаунта"):
        authorized_driver.get("https://ru.yougile.com/team/settings-account")

    with allure.step("Поиск поля с отображаемым именем"):
        user_name = authorized_driver.find_element(
            By.CSS_SELECTOR, "[placeholder='Отображаемое имя…']")

    with allure.step("Проверка отображения поля и корректности имени 'Юлия'"):
        assert user_name.is_displayed(), ("Поле с именем"
                                          " пользователя не отображается")
        actual_name = user_name.get_attribute("value")
        assert actual_name == "Юлия", (f"Ожидалось имя 'Юлия', "
                                       f"но получено '{actual_name}'")
