"""Funkcje pomocnicze dla formularza rejestracji SklepTO."""
import itertools

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from konfiguracja import SKLEPTO_URL

# reprezentanci klas POPRAWNYCH (login: unikalny_login())
POPRAWNE = {"email": "nowy@example.com", "wiek": "30",
            "haslo": "Haslo123", "haslo2": None, "regulamin": True}

SUKCES = "Konto zostało utworzone. Możesz się zalogować."
KOMUNIKATY = {
    "login": "Login musi mieć od 3 do 20 znaków "
             "(małe litery, cyfry, _).",
    "email": "Niepoprawny adres e-mail.",
    "wiek": "Wiek musi być liczbą całkowitą z zakresu 18–99.",
    "haslo": "Hasło musi mieć od 8 do 20 znaków "
             "i zawierać literę oraz cyfrę.",
    "haslo2": "Hasła nie są identyczne.",
    "regulamin": "Musisz zaakceptować regulamin.",
}

SUKCES_LOK = (By.ID, "sukces")
BLEDY_LOK = (By.ID, "bledy")
_licznik = itertools.count(1)


def unikalny_login(dlugosc=10):
    """Poprawny login o zadanej długości, za każdym razem inny."""
    login = str(next(_licznik)).rjust(dlugosc, "u")
    assert len(login) == dlugosc, "licznik dłuższy niż login"
    return login


def haslo_o_dlugosci(dlugosc):
    """Hasło z literą i cyfrą, np. 8 -> 'aaaaaaa1'."""
    return "a" * (dlugosc - 1) + "1"


def zarejestruj(driver, **zmiany):
    """Wypełnia i wysyła formularz; zmiany nadpisują POPRAWNE."""
    dane = {**POPRAWNE, **zmiany}
    dane.setdefault("login", unikalny_login())
    if dane["haslo2"] is None:
        dane["haslo2"] = dane["haslo"]
    driver.get(f"{SKLEPTO_URL}/rejestracja.php")
    wiek = driver.find_element(By.ID, "wiek")
    # type=number nie przyjmuje liter – testujemy walidację SERWERA
    driver.execute_script("arguments[0].type = 'text';", wiek)
    for pole in ("login", "email", "wiek", "haslo", "haslo2"):
        element = driver.find_element(By.ID, pole)
        element.clear()
        element.send_keys(dane[pole])
    if dane["regulamin"]:
        driver.find_element(By.ID, "regulamin").click()
    driver.find_element(By.ID, "zarejestruj").click()
    # skutek wysłania: NOWA strona z #sukces albo z listą #bledy
    WebDriverWait(driver, 10).until(
        EC.any_of(EC.presence_of_element_located(SUKCES_LOK),
                  EC.presence_of_element_located(BLEDY_LOK)),
        message="Brak #sukces i #bledy po wysłaniu formularza")


def bledy(driver):
    """Słownik {pole: komunikat} z listy ul#bledy."""
    elementy = driver.find_elements(By.CSS_SELECTOR, "li.blad")
    return {li.get_attribute("data-pole"): li.text
            for li in elementy}


def sukces(driver):
    """Tekst komunikatu #sukces albo None."""
    elementy = driver.find_elements(*SUKCES_LOK)
    return elementy[0].text if elementy else None


def oczekuj_sukcesu(driver):
    assert bledy(driver) == {}
    assert sukces(driver) == SUKCES


def oczekuj_bledu(driver, pole, komunikat=None):
    """Dokładnie jeden błąd – dla pola z klasą niepoprawną."""
    assert sukces(driver) is None
    assert bledy(driver) == {pole: komunikat or KOMUNIKATY[pole]}


def sprawdz_wynik(driver, pole, poprawna):
    if poprawna:
        oczekuj_sukcesu(driver)
    else:
        oczekuj_bledu(driver, pole)
