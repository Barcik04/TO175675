"""Analiza wartości brzegowych (AWB): 2- i 3-punktowa."""
import pytest

from formularz import (haslo_o_dlugosci, sprawdz_wynik,
                       unikalny_login, zarejestruj)

# znany defekt: wiek 100 jest przyjmowany (DEF-REJ-01)
DEF_REJ_01 = pytest.mark.xfail(reason="DEF-REJ-01", strict=True)
WIEK_DEFEKTY = {100: DEF_REJ_01}

# (wartość, czy należy do klasy poprawnej)
WIEK_2P = [(17, False), (18, True), (99, True), (100, False)]
WIEK_3P = [(17, False), (18, True), (19, True),
           (98, True), (99, True), (100, False)]
LOGIN_2P = [(2, False), (3, True), (20, True), (21, False)]
LOGIN_3P = [(2, False), (3, True), (4, True),
            (19, True), (20, True), (21, False)]
HASLO_2P = [(7, False), (8, True), (20, True), (21, False)]
HASLO_3P = [(7, False), (8, True), (9, True),
            (19, True), (20, True), (21, False)]


def przypadki(dane, defekty=None):
    defekty = defekty or {}
    return [pytest.param(w, ok, id=str(w), marks=defekty.get(w, ()))
            for w, ok in dane]


@pytest.mark.parametrize("wiek, poprawna",
                         przypadki(WIEK_2P, WIEK_DEFEKTY))
def test_wiek_2p(driver, wiek, poprawna):
    zarejestruj(driver, wiek=str(wiek))
    sprawdz_wynik(driver, "wiek", poprawna)


@pytest.mark.parametrize("wiek, poprawna",
                         przypadki(WIEK_3P, WIEK_DEFEKTY))
def test_wiek_3p(driver, wiek, poprawna):
    zarejestruj(driver, wiek=str(wiek))
    sprawdz_wynik(driver, "wiek", poprawna)


@pytest.mark.parametrize("dl, poprawna", przypadki(LOGIN_2P))
def test_login_dlugosc_2p(driver, dl, poprawna):
    zarejestruj(driver, login=unikalny_login(dl))
    sprawdz_wynik(driver, "login", poprawna)


@pytest.mark.parametrize("dl, poprawna", przypadki(LOGIN_3P))
def test_login_dlugosc_3p(driver, dl, poprawna):
    zarejestruj(driver, login=unikalny_login(dl))
    sprawdz_wynik(driver, "login", poprawna)


@pytest.mark.parametrize("dl, poprawna", przypadki(HASLO_2P))
def test_haslo_dlugosc_2p(driver, dl, poprawna):
    zarejestruj(driver, haslo=haslo_o_dlugosci(dl))
    sprawdz_wynik(driver, "haslo", poprawna)


@pytest.mark.parametrize("dl, poprawna", przypadki(HASLO_3P))
def test_haslo_dlugosc_3p(driver, dl, poprawna):
    zarejestruj(driver, haslo=haslo_o_dlugosci(dl))
    sprawdz_wynik(driver, "haslo", poprawna)