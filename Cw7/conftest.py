"""Fixture: przeglądarka i stan bazy danych SklepTO."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from konfiguracja import SKLEPTO_URL

# czytelne komunikaty asercji także w module pomocniczym
pytest.register_assert_rewrite("formularz")


@pytest.fixture(scope="session")
def driver():
    """Jedna przeglądarka na całą sesję testów (szybciej)."""
    drv = webdriver.Chrome()
    drv.implicitly_wait(0)
    yield drv
    drv.quit()


def resetuj_baze(driver):
    driver.get(f"{SKLEPTO_URL}/install.php?reset=1")
    status = driver.find_element(By.ID, "install-status").text
    assert status == "OK", "Reset bazy nieudany – czy działa MySQL?"


@pytest.fixture(scope="session", autouse=True)
def baza_poczatkowa(driver):
    """Raz na sesję: dane startowe (jan, anna, zablokowany)."""
    resetuj_baze(driver)



@pytest.fixture
def czysta_baza(driver):
    """Na żądanie: stan początkowy bazy tuż przed testem."""
    resetuj_baze(driver)


@pytest.fixture(autouse=True)
def bez_ciasteczek(driver):
    """Każdy test zaczyna bez sesji PHP (niezależność testów)."""
    driver.delete_all_cookies()