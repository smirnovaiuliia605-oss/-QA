import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1. Фикстура для инициализации и гарантированного закрытия браузера
@pytest.fixture
def driver():
    with allure.step("Запуск браузера Chrome"):
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()

    yield chrome_driver  # Здесь выполняется сам тест

    with allure.step("Закрытие браузера"):
        chrome_driver.quit()


# 2. Передаем имя фикстуры 'driver' в качестве аргумента теста
@allure.epic("Управление компанией")
@allure.feature("Отделы")
@allure.story("Редактирование названия отдела")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_department_name(driver):
    wait = WebDriverWait(driver, 25)

    with allure.step("Открытие главной страницы авторизации YouGile"):
        driver.get("https://ru.yougile.com/team/")

    current_dept_name = "Тестирование"
    updated_dept_name = "Новый отдел тестирования"

    with (allure.step("Авторизация в системе")):
        with allure.step("Ввод email"):
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[autocomplete='email']")
            )).send_keys("smirnova_iuliia@list.ru")

        with allure.step("Ввод пароля"):
            driver.find_element(
                By.CSS_SELECTOR, "[autocomplete='current-password']"
            ).send_keys("q52nyZvET!8A_7k")

        with allure.step("Нажатие кнопки 'Войти'"):
            driver.find_element(
                By.CSS_SELECTOR, ".bg-action-default[role='button']").click()

    with (allure.step("Ожидание авторизации и переход в настройки аккаунта")):
        wait.until(EC.url_contains("team"))
        driver.get("https://ru.yougile.com/team/settings-account")

        with allure.step(
                f"Поиск строки существующего отдела"
                f" '{current_dept_name}' в списке"):
            department_row = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{current_dept_name}')]"
                           f"/ancestor::div[contains(@class, 'row')]")
            ))
        with allure.step("Прокрутка страницы к выбранному отделу"):
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                department_row)

        with allure.step("Нажатие кнопки 'Редактировать'"):
            edit_btn = department_row.find_element(
                By.XPATH, ".//button[contains(@class, 'edit')]")
            edit_btn.click()

        with allure.step("Очистка старого названия и ввод нового"):
            name_input = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f"input[value='{current_dept_name}'], "
                                  f"input[placeholder*='название']")
            ))
            name_input.clear()
            name_input.send_keys(updated_dept_name)

        with allure.step("Нажатие кнопки 'Сохранить изменения'"):
            save_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Сохранить изменения')]")
            ))
            save_btn.click()

        with allure.step(
                f"Ожидание исчезновения старого названия "
                f"'{current_dept_name}'"):
            wait.until(EC.invisibility_of_element_located(
                (By.XPATH, f"//*[text()='{current_dept_name}']")
            ))

        with allure.step(f"Проверка появления нового названия"
                         f" '{updated_dept_name}' в списке"):
            updated_dept_element = wait.until(EC.visibility_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{updated_dept_name}')]")
            ))
            assert updated_dept_element.is_displayed(), (
                f"Новое название '{updated_dept_name}' "
                f"не отображается на странице!")
