from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

URBAN_ID = "SIDO_NM0"
SUB_URBAN_ID = "SIGUNGU_NM0"
DOWNLOAD_ELEM_ID = "glopopd_excel"


def get_available_element(driver, elem_id, timeout=5):
    loc = (By.ID, elem_id)
    availability = expected_conditions.element_to_be_clickable(loc)
    WebDriverWait(driver, timeout).until(availability)
    return driver.find_element(By.ID, elem_id)


def wait_modal_twinkle(driver):
    modal_window = driver.find_element(By.ID, "modalwindow")
    modal_display = expected_conditions.visibility_of(modal_window)
    WebDriverWait(driver, timeout=5).until(modal_display)
    modal_not_display = expected_conditions.invisibility_of_element(
        modal_window)
    WebDriverWait(driver, timeout=5).until(modal_not_display)


def wait_download_ready(driver):
    WebDriverWait(driver, timeout=5).until(lambda d: d.execute_script(
        "return typeof NetFunnel_Action === \"function\"") == True)


def get_sub_urbans(driver):
    sub_urbans = []
    elements = Select(get_available_element(driver, SUB_URBAN_ID)).options
    for element in elements:
        if element.get_attribute("value") == "":
            continue
        sub_urbans.append(element.get_attribute("value"))
    return sub_urbans


driver = webdriver.Chrome()
driver.get("https://www.opinet.co.kr/searRgSelect.do")

urban = get_available_element(driver, URBAN_ID)
Select(urban).select_by_value("서울특별시")

targets = get_sub_urbans(driver)
while len(targets) > 0:
    target_value = targets.pop()
    sub_urban = get_available_element(driver, SUB_URBAN_ID)
    Select(sub_urban).select_by_value(target_value)

    wait_download_ready(driver)

    excel_down = get_available_element(driver, DOWNLOAD_ELEM_ID)
    excel_down.click()

    wait_modal_twinkle(driver)

driver.quit()
