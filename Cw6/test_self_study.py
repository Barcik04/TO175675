from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import INTERNET_URL


def test_task1_loading_indicator(driver):
    driver.get(f"{INTERNET_URL}/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "loading")))
    wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
    assert driver.find_element(By.CSS_SELECTOR, "#finish h4").text == "Hello World!"


def test_task2_enable_input_and_type(driver):
    driver.get(f"{INTERNET_URL}/dynamic_controls")
    driver.find_element(By.CSS_SELECTOR, "#input-example button").click()
    field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input"))
    )
    field.send_keys("Selenium")
    assert field.get_attribute("value") == "Selenium"


def test_task3_prompt_cancel(driver):
    driver.get(f"{INTERNET_URL}/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.dismiss()
    assert driver.find_element(By.ID, "result").text == "You entered: null"