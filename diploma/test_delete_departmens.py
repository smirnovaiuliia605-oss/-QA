import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    with allure.step("Запуск браузера Chrome"):
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()

    yield chrome_driver

    with allure.step("Закрытие браузера"):
        chrome_driver.quit()


@allure.epic("Управление компанией")
@allure.feature("Отделы")
@allure.story("Удаление существующего отдела")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_department(driver):
    wait = WebDriverWait(driver, 25)

    with allure.step("Открытие главной страницы авторизации YouGile"):
        driver.get("https://ru.yougile.com/team/")

    dept_to_delete = "Новый отдел тестирования"

    with allure.step("Авторизация в системе"):
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

    with allure.step("Ожидание авторизации и переход в настройки аккаунта"):
        wait.until(EC.url_contains("team"))
        driver.get("https://ru.yougile.com/team/settings-account")

        with allure.step(f"Поиск строки отдела '{dept_to_delete}' в списке"):
            department_row = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{dept_to_delete}')]"
                           f"/ancestor::div[contains(@class, 'row')]")
            ))

        with allure.step("Прокрутка страницы к выбранному отделу"):
            driver.execute_script(
                "arguments.scrollIntoView({block: 'center'});",
                department_row)

        with allure.step("Нажатие кнопки 'Удалить отдел' "
                         "внутри строки отдела"):
            delete_btn = department_row.find_element(
                By.XPATH, ".//button[contains(@class, 'delete')]")
            delete_btn.click()

        with allure.step("Подтверждение удаления в модальном окне"):
            confirm_delete_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, 'modal')]"
                           "//button[contains(., 'Удалить')]")
            ))
            confirm_delete_btn.click()

        with allure.step("Ожидание исчезновения отдела из списка"):
            is_deleted = wait.until(EC.invisibility_of_element_located(
                (By.XPATH, f"//*[text()='{dept_to_delete}']")
            ))

        with allure.step("Проверка успешности удаления"):
            assert is_deleted, (f"Ошибка: "
                                f"Отдел '{dept_to_delete}' не был удален!")
