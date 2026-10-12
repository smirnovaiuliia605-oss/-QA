import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Управление компанией")
@allure.feature("Отделы")
@allure.story("Добавление нового отдела компании")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_company_department(authorized_driver):
    wait = WebDriverWait(authorized_driver, 25)

    with allure.step("Переход в настройки аккаунта"):
        authorized_driver.get("https://ru.yougile.com/team/settings-account")

    with allure.step("Переход во вкладку 'Моя компания'"):
        my_company_tab = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//a[contains(@href, 'company')]"
        )))
        my_company_tab.click()
