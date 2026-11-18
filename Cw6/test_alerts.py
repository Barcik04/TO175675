"""JavaScript dialogs: alert, confirm, prompt."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import INTERNET_URL


def click_button(driver, text):
    """Opens /javascript_alerts, clicks the button, returns the dialog."""
    driver.get(f"{INTERNET_URL}/javascript_alerts")
    driver.find_element(By.XPATH, f"//button[text()='{text}']").click()
    return WebDriverWait(driver, 5).until(EC.alert_is_present())


def result_text(driver):
    return driver.find_element(By.ID, "result").text


def test_alert(driver):
    alert = click_button(driver, "Click for JS Alert")
    assert alert.text == "I am a JS Alert"
    alert.accept()
    assert result_text(driver) == "You successfully clicked an alert"


@pytest.mark.parametrize("accept, expected", [
    (True, "You clicked: Ok"),
    (False, "You clicked: Cancel"),
], ids=["ok", "cancel"])
def test_confirm(driver, accept, expected):
    """Step 4: OK -> accept(), Cancel -> dismiss()."""
    alert = click_button(driver, "Click for JS Confirm")
    if accept:
        alert.accept()
    else:
        alert.dismiss()
    assert result_text(driver) == expected

def test_prompt(driver):
    """Step 4: type 'Selenium' and accept."""
    alert = click_button(driver, "Click for JS Prompt")
    alert.send_keys("Selenium")
    alert.accept()
    assert result_text(driver) == "You entered: Selenium"
