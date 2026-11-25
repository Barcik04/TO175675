from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from formularz import (POPRAWNE, oczekuj_sukcesu, unikalny_login,
                       zarejestruj)
from konfiguracja import SKLEPTO_URL


def test_dane_konta_w_admin(driver):
    login = unikalny_login()
    zarejestruj(driver, login=login, email="nowy@example.com", wiek="30")
    oczekuj_sukcesu(driver)
    driver.get(f"{SKLEPTO_URL}/admin.php")
    wiersz = driver.find_element(
        By.CSS_SELECTOR, f"#uzytkownicy tr[data-login='{login}']")
    assert wiersz.find_element(By.CLASS_NAME, "email").text == "nowy@example.com"
    assert wiersz.find_element(By.CLASS_NAME, "wiek").text == "30"


def test_nowe_konto_mozna_zalogowac(driver):
    login = unikalny_login()
    zarejestruj(driver, login=login)
    oczekuj_sukcesu(driver)
    driver.get(f"{SKLEPTO_URL}/logowanie.php")
    driver.find_element(By.ID, "login").send_keys(login)
    driver.find_element(By.ID, "haslo").send_keys(POPRAWNE["haslo"])
    driver.find_element(By.ID, "zaloguj").click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"), "Zalogowano jako"),
        message="Brak komunikatu „Zalogowano jako" "po zalogowaniu")
    tekst = driver.find_element(By.TAG_NAME, "body").text
    assert f"Zalogowano jako {login}" in tekst