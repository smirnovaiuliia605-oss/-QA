import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    chrome_driver = None
    with allure.step("Запуск браузера Chrome"):
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()
    yield chrome_driver
    if chrome_driver:
        with allure.step("Закрытие браузера"):
            chrome_driver.quit()


@allure.epic("Авторизация")
@allure.feature("Вход через сторонние сервисы")
@allure.story("Успешная авторизация через VK ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_yougile_auth_vk(driver):
    wait = WebDriverWait(driver, 25)

    with allure.step("Открытие главной страницы авторизации YouGile"):
        driver.get("https://ru.yougile.com/team/")
        original_window = driver.current_window_handle

    with allure.step("Клик по кнопке авторизации через VK"):
        vk_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "a[href*='://vk.com'], [class*='IconButton']"
        )))
        vk_btn.click()

    with allure.step("Ожидание открытия и переключение на окно VK ID"):
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

    with allure.step("Авторизация на стороне VK ID"):
        email_input = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "input[name='login'], input[autocomplete='email']"
        )))
        email_input.send_keys("smirnova_iuliia@list.ru")

        password_input = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "input[name='password'], "
                             "input[autocomplete='current-password']"
        )))
        password_input.send_keys("q52nyZvET!8A_7k")

        submit_vk = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[type='submit'], .vkuiButton__content"
        )))
        submit_vk.click()

    with allure.step("Возврат к исходному окну "
                     "YouGile и ожидание авторизации"):
        driver.switch_to.window(original_window)

    with allure.step("Поиск поля с отображаемым именем"):
        user_name = wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "[placeholder='Отображаемое имя…']"
        )))

    with allure.step("Проверка корректности имени пользователя после входа"):
        actual_name = user_name.get_attribute("value")
        assert actual_name == "Юлия", \
            f"Ожидалось имя 'Юлия', но получено '{actual_name}'"
