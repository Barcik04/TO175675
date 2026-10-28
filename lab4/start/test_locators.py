"""DevTools exercise: CSS and XPath locators.

Fill in the table: for each element enter a CSS selector
and an XPath expression (checked in DevTools: $$() and $x()).
"""
import pytest
from selenium.webdriver.common.by import By
from config import INTERNET_URL, SELENIUM_WEB_URL
from helpers import open_page

I, W = INTERNET_URL, SELENIUM_WEB_URL + "/web-form.html"
LOCATORS = [
    (I + "/login", "#username", "//input[@id='username']"),                      # 1
    (I + "/login", "button[type='submit']", "//button[@type='submit']"),          # 2
    (I + "/login", "label[for='password']", "//label[@for='password']"),          # 3
    (I + "/checkboxes", "#checkboxes input:nth-of-type(2)", "(//input[@type='checkbox'])[2]"),  # 4
    (I + "/tables", "#table2 tbody tr:nth-of-type(3) td.email", "//table[@id='table2']//tr[td[text()='Doe']]/td[@class='email']"), # 5
    (I + "/tables", "#table1 th:nth-of-type(4)", "//table[@id='table1']//th[span[text()='Due']]"),  # 6
    (I + "/add_remove_elements/", "button[onclick='addElement()']", "//button[text()='Add Element']"),  # 7
    (W, "#my-text-id", "//input[@id='my-text-id']"),                              # 8
    (W, "input[name='my-disabled']", "//input[@name='my-disabled']"),             # 9
    (W, "select[name='my-select'] option[value='2']", "//select[@name='my-select']/option[text()='Two']"),  # 10
    (W, "button[type='submit']", "//button[@type='submit']"),                     # 11
    (W, "a[href='./index.html']", "//a[contains(., 'Return to index')]"),  # 12
]
@pytest.mark.parametrize("url, css, xpath", LOCATORS)
def test_css_and_xpath(driver, url, css, xpath):
    if not css or not xpath:
        pytest.skip("TODO: fill in the locators")
    open_page(driver, url, By.CSS_SELECTOR, "#content, form")
    by_css = driver.find_elements(By.CSS_SELECTOR, css)
    by_xpath = driver.find_elements(By.XPATH, xpath)
    assert len(by_css) == 1, "CSS: expected exactly 1 element"
    assert len(by_xpath) == 1, "XPath: expected exactly 1 element"
    assert by_css[0] == by_xpath[0]           # the same element
