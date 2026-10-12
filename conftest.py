import os
import pytest
import allure
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


@pytest.fixture(scope="session")
def browser():
    with allure.step("Запуск браузера Chrome (Глобальный)"):
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()

    yield chrome_driver

    with allure.step("Закрытие браузера (Глобальный)"):
        chrome_driver.quit()


@pytest.fixture(scope="session")
def authorized_driver(browser):
    wait = WebDriverWait(browser, 25)

    with allure.step("Глобальная авторизация в YouGile"):
        browser.get("https://ru.yougile.com/team/settings-account")

        email = os.getenv("YOUGILE_EMAIL")
        password = os.getenv("YOUGILE_PASSWORD")

        email_input = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "input[autocomplete='email'], input[type='email']"
        )))
        email_input.send_keys(email)

        password_input = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "input[autocomplete='current-password'], "
                             "input[type='password']"
        )))
        password_input.send_keys(password)

        login_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[type='submit'], "
                             ".bg-action-default[role='button']"
        )))
        login_btn.click()

        wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "a[href*='settings'], "
                             "[class*='User'], [class*='sidebar']"
        )))

    return browser
