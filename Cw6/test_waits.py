"""Synchronisation: sleep vs implicit wait vs explicit wait."""
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import INTERNET_URL

START = (By.CSS_SELECTOR, "#start button")
RESULT = (By.CSS_SELECTOR, "#finish h4")


@pytest.mark.slow
def test_sleep_anti_pattern(driver):
    driver.get(f"{INTERNET_URL}/dynamic_loading/2")
    driver.find_element(*START).click()
    time.sleep(6)                   # ANTI-PATTERN: always 6 seconds
    assert driver.find_element(*RESULT).text == "Hello World!"


@pytest.mark.parametrize("example", [1, 2])
def test_explicit_wait(driver, example):
    """Step 1: WebDriverWait + EC.visibility_of_element_located(RESULT)."""
    driver.get(f"{INTERNET_URL}/dynamic_loading/{example}")
    driver.find_element(*START).click()
    wait = WebDriverWait(driver, timeout=10)
    heading = wait.until(EC.visibility_of_element_located(RESULT))
    assert heading.text == "Hello World!"


def test_implicit_wait_example_2(driver):
    driver.implicitly_wait(10)      # applies to every find_element
    driver.get(f"{INTERNET_URL}/dynamic_loading/2")
    driver.find_element(*START).click()
    assert driver.find_element(*RESULT).text == "Hello World!"


@pytest.mark.xfail(strict=True,
                   reason="implicit wait waits for presence in the DOM, "
                          "not for visibility")
def test_implicit_wait_example_1(driver):
    driver.implicitly_wait(10)
    driver.get(f"{INTERNET_URL}/dynamic_loading/1")
    driver.find_element(*START).click()
    # the element is in the DOM from the start (hidden) -> text == ""
    assert driver.find_element(*RESULT).text == "Hello World!"
