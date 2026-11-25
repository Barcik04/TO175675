"""Testy sterowane danymi z plików CSV i JSON (katalog dane/)."""
import csv
from pathlib import Path

import pytest

from formularz import sprawdz_wynik, zarejestruj

DANE = Path(__file__).parent / "dane"

# znane defekty: wiek 100 (DEF-REJ-01), login z wielką literą (DEF-REJ-02)
DEF_REJ_01 = pytest.mark.xfail(reason="DEF-REJ-01", strict=True)
DEF_REJ_02 = pytest.mark.xfail(reason="DEF-REJ-02", strict=True)


def wczytaj_csv(nazwa, defekty=None):
    """Wiersze CSV (separator ;) jako pytest.param z id."""
    defekty = defekty or {}
    with open(DANE / nazwa, encoding="utf-8-sig", newline="") as f:
        wiersze = list(csv.DictReader(f, delimiter=";"))
    return [pytest.param(w["wartosc"], w["wynik"] == "OK",
                         id=w["id"], marks=defekty.get(w["id"], ()))
            for w in wiersze]


@pytest.mark.parametrize(
    "wiek, poprawna",
    wczytaj_csv("wiek.csv", {"AWB-100": DEF_REJ_01}))
def test_wiek_z_csv(driver, wiek, poprawna):
    zarejestruj(driver, wiek=wiek)
    sprawdz_wynik(driver, "wiek", poprawna)


@pytest.mark.parametrize(
    "login, poprawna",
    wczytaj_csv("login.csv", {"EP-wielkie-litery": DEF_REJ_02}))
def test_login_z_csv(driver, login, poprawna):
    zarejestruj(driver, login=login)
    sprawdz_wynik(driver, "login", poprawna)


# TODO (*): wczytaj_json + test_email_z_json – dane/email.json