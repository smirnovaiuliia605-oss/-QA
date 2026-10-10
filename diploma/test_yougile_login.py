import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    with allure.step("Запуск браузера Chrome"):
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()

    yield chrome_driver

    with allure.step("Закрытие браузера"):
        chrome_driver.quit()


@allure.epic("Авторизация")
@allure.feature("Вход в систему")
@allure.story("Успешная авторизация и проверка имени пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_yougile_login():
    with (allure.step("Запуск браузера Chrome")):
        driver = webdriver.Chrome()
        driver.maximize_window()

        with allure.step("Открытие главной страницы авторизации YouGile"):
            driver.get("https://ru.yougile.com/team/")

        with allure.step("Ввод email"):
            email_input = driver.find_element(
                By.CSS_SELECTOR, "[autocomplete='email']")
            email_input.send_keys("smirnova_iuliia@list.ru")

        with allure.step("Ввод пароля"):
            password_input = driver.find_element(
                By.CSS_SELECTOR, "[autocomplete='current-password']")
            password_input.send_keys("q52nyZvET!8A_7k")

        with allure.step("Нажатие кнопки 'Войти'"):
            login_button = driver.find_element(
                By.CSS_SELECTOR, ".bg-action-default[role='button']")
            login_button.click()

        with allure.step("Переход в настройки аккаунта"):
            driver.get("https://ru.yougile.com/team/settings-account")

        with allure.step("Поиск поля с отображаемым именем"):
            user_name = driver.find_element(
                By.CSS_SELECTOR, "[placeholder='Отображаемое имя…']")

        with allure.step("Проверка отображения поля "
                         "и корректности имени 'Юлия'"):
            assert user_name.is_displayed(), ("Поле с именем "
                                              "пользователя не отображается")
            actual_name = user_name.get_attribute("value")
            assert actual_name == "Юлия", (f"Ожидалось имя 'Юлия', "
                                           f"но получено '{actual_name}'")

        with allure.step("Закрытие браузера"):
            driver.quit()
