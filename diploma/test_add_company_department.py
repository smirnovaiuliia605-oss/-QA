import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = None
    try:
        with allure.step("Запуск браузера Chrome"):
            chrome_driver = webdriver.Chrome()
            chrome_driver.maximize_window()
        yield chrome_driver
    finally:
        if chrome_driver:
            with allure.step("Закрытие браузера"):
                chrome_driver.quit()


@allure.epic("Управление компанией")
@allure.feature("Отделы")
@allure.story("Добавление нового отдела компании")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_company_department(driver):
    wait = WebDriverWait(driver, 25)

    with allure.step("Открытие главной страницы авторизации YouGile"):
        driver.get("https://ru.yougile.com/team/")

    with allure.step("Авторизация в системе"):
        with allure.step("Ввод email"):
            wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, "input[autocomplete='email'], "
                                 "input[type='email']"
            ))).send_keys("smirnova_iuliia@list.ru")

        with allure.step("Ввод пароля"):
            wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, "input[autocomplete='current-password'], "
                                 "input[type='password']"
            ))).send_keys("q52nyZvET!8A_7k")

        with allure.step("Нажатие кнопки 'Войти'"):
            login_btn = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, "button[type='submit'], "
                                 ".bg-action-default[role='button']"
            )))
            login_btn.click()

        with allure.step("Ожидание появления интерфейса личного кабинета"):

            wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "a[href*='settings'], "
                                 "[class*='User'], [class*='sidebar']"
            )))

    with allure.step("Переход в настройки аккаунта"):

        driver.get("https://ru.yougile.com/team/settings-account")

    with allure.step("Переход во вкладку 'Моя компания'"):

        my_company_tab = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//a[contains(@href, 'company')]"
        )))
        my_company_tab.click()
