import os
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Авторизация")
@allure.feature("Вход через сторонние сервисы")
@allure.story("Успешная авторизация через VK ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_yougile_auth_vk(browser):
    wait = WebDriverWait(browser, 25)

    with allure.step("Открытие главной страницы авторизации YouGile"):
        browser.get("https://ru.yougile.com/team/settings-account")
        original_window = browser.current_window_handle

    with allure.step("Клик по кнопке авторизации через VK"):
        vk_btn = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "a[href*='://vk.com'], [class*='IconButton']"
        )))
        vk_btn.click()

    with allure.step("Ожидание открытия и переключение на окно VK ID"):
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in browser.window_handles:
            if window_handle != original_window:
                browser.switch_to.window(window_handle)
                break

    with allure.step("Авторизация на стороне VK ID"):
        email_input = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "input[name='login'], input[autocomplete='email']"
        )))
        vk_email = os.getenv("YOUGILE_EMAIL")
        email_input.send_keys(vk_email)

        password_input = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "input[name='password'], "
                             "input[autocomplete='current-password']"
        )))
        vk_password = os.getenv("YOUGILE_PASSWORD")
        password_input.send_keys(vk_password)

        submit_vk = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[type='submit'], .vkuiButton__content"
        )))
        submit_vk.click()

    with allure.step("Возврат к исходному окну YouGile "
                     "и ожидание авторизации"):
        browser.switch_to.window(original_window)

    with allure.step("Поиск поля с отображаемым именем"):
        user_name = wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "[placeholder='Отображаемое имя…']"
        )))

    with allure.step("Проверка корректности имени пользователя после входа"):
        actual_name = user_name.get_attribute("value")
        assert actual_name == "Юлия", (f"Ожидалось имя 'Юлия', "
                                       f"но получено '{actual_name}'")
