"""Frames and browser windows."""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import INTERNET_URL


def body_text(driver):
    return driver.find_element(By.TAG_NAME, "body").text


def h3_text(driver):
    return driver.find_element(By.TAG_NAME, "h3").text


def test_nested_frames(driver):
    """Step 5: read LEFT, MIDDLE and BOTTOM."""
    driver.get(f"{INTERNET_URL}/nested_frames")
    driver.switch_to.frame("frame-top")          # by name
    driver.switch_to.frame("frame-left")         # a frame inside a frame
    assert body_text(driver) == "LEFT"
    driver.switch_to.parent_frame()              # back to frame-top
    driver.switch_to.frame(1)                    # by index: frame-middle
    assert body_text(driver) == "MIDDLE"
    driver.switch_to.default_content()           # back to the page
    driver.switch_to.frame("frame-bottom")
    assert body_text(driver) == "BOTTOM"


def test_new_window(driver):
    """Step 6: Click Here -> 'New Window' -> close -> back."""
    driver.get(f"{INTERNET_URL}/windows")
    main = driver.current_window_handle
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    new = [h for h in driver.window_handles if h != main][0]
    driver.switch_to.window(new)
    assert h3_text(driver) == "New Window"
    driver.close()                      # closes the new one only
    driver.switch_to.window(main)
    assert h3_text(driver) == "Opening a new window"