from selenium.webdriver.common.by import By
from config import INTERNET_URL, SELENIUM_WEB_URL
from helpers import open_page, wait_for
import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.relative_locator import locate_with
from helpers import open_page

def test_wrong_username_and_password(driver):
    """1. /login: zły login i złe hasło – który komunikat?"""
    open_page(driver, f"{INTERNET_URL}/login", By.ID, "login")
    driver.find_element(By.ID, "username").send_keys("tomek")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR, "#login button").click()
    flash = wait_for(driver, By.ID, "flash")
    print("MESSAGE:", flash.text)      # visible with: pytest -s
    assert "Your username is invalid!" in flash.text


def test_check_only_unchecked(driver):
    """2. /checkboxes: pętlą for zaznacz tylko niezaznaczone."""
    open_page(driver, f"{INTERNET_URL}/checkboxes", By.ID, "checkboxes")
    boxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input")
    for box in boxes:
        if not box.is_selected():
            box.click()
    assert len(boxes) == 2
    assert all(box.is_selected() for box in boxes)


def test_range_default_value(driver):
    """3. Web Form: suwak my-range – value domyślnie 5."""
    open_page(driver, f"{SELENIUM_WEB_URL}/web-form.html", By.TAG_NAME, "form")
    slider = driver.find_element(By.NAME, "my-range")
    assert slider.get_property("value") == "5"


def test_button_css_color(driver):
    """4. Web Form: value_of_css_property("color") przycisku."""
    open_page(driver, f"{SELENIUM_WEB_URL}/web-form.html", By.TAG_NAME, "form")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    color = button.value_of_css_property("color")
    print("COLOR:", color)             # visible with: pytest -s
    assert color.startswith("rgba(")






def test_all_emails_contain_at(driver):
    """5. /tables: każdy e-mail w tabeli 1 zawiera „@”."""
    open_page(driver, f"{INTERNET_URL}/tables", By.ID, "table1")
    cells = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody td:nth-child(3)")
    emails = [td.text for td in cells]
    print("EMAILS:", emails)
    assert len(emails) == 4
    assert all("@" in email for email in emails)


def test_locate_with_below_username(driver):
    """6. locate_with: pole poniżej #username na /login."""
    username = open_page(driver, f"{INTERNET_URL}/login", By.ID, "username")
    below = driver.find_element(locate_with(By.TAG_NAME, "input").below(username))
    assert below.get_dom_attribute("id") == "password"


# 7. Fixture z scope="module": zmierz czas, oceń ryzyko.
@pytest.fixture(scope="module")
def shared_driver():
    start = time.perf_counter()
    drv = webdriver.Chrome()
    print(f"\nSETUP (browser start, once): {time.perf_counter() - start:.2f}s")
    yield drv
    drv.quit()


def test_module_fixture_first(shared_driver):
    start = time.perf_counter()
    open_page(shared_driver, f"{INTERNET_URL}/login", By.ID, "login")
    print(f"\nTEST 1 took: {time.perf_counter() - start:.2f}s")
    assert shared_driver.current_url.endswith("/login")


def test_module_fixture_second(shared_driver):
    start = time.perf_counter()
    open_page(shared_driver, f"{INTERNET_URL}/checkboxes", By.ID, "checkboxes")
    print(f"\nTEST 2 took: {time.perf_counter() - start:.2f}s")
    assert shared_driver.current_url.endswith("/checkboxes")


def test_send_keys_to_disabled_raises(driver):
    """8. send_keys na polu disabled – jaki wyjątek? Test z pytest.raises."""
    open_page(driver, f"{SELENIUM_WEB_URL}/web-form.html", By.TAG_NAME, "form")
    disabled = driver.find_element(By.NAME, "my-disabled")
    with pytest.raises(ElementNotInteractableException):
        disabled.send_keys("XYZ")