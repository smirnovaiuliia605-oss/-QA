import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Управление компанией")
@allure.feature("Отделы")
@allure.story("Редактирование названия отдела")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_department_name(authorized_driver):
    wait = WebDriverWait(authorized_driver, 25)

    current_dept_name = "Тестирование"
    updated_dept_name = "Новый отдел тестирования"

    with allure.step("Переход в настройки аккаунта"):
        authorized_driver.get("https://ru.yougile.com/team/settings-account")

    with allure.step(f"Поиск строки существующего отдела"
                     f" '{current_dept_name}' в списке"):
        department_row = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{current_dept_name}')]"
                       f"/ancestor::div[contains(@class, 'row')]")
        ))

    with allure.step("Прокрутка страницы к выбранному отделу"):
        authorized_driver.execute_script(
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

    with allure.step(f"Ожидание исчезновения старого названия"
                     f" '{current_dept_name}'"):
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
