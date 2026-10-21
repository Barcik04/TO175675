"""Testy czarnoskrzynkowe: ticket_price (BL-1 ... BL-4)."""
import pytest

from sut import ticket_price


# EP – klasy poprawne: jedna typowa wartość z każdej klasy WEJŚCIA
# (uwaga: cena 10.0 dotyczy dwóch różnych grup wieku)
@pytest.mark.parametrize("age, price", [
    pytest.param(3, 0.0, id="free"),
    pytest.param(12, 10.0, id="reduced_youth"),
    pytest.param(40, 20.0, id="normal"),
    pytest.param(70, 10.0, id="reduced_senior"),
])
def test_ep_valid_classes(age, price):
    assert ticket_price(age) == price


# EP – klasy niepoprawne (wartość): jeden test = jedna klasa
@pytest.mark.parametrize("age", [
    pytest.param(-1, id="negative"),
    pytest.param(150, id="above_120"),
])
def test_ep_out_of_range(age):
    with pytest.raises(ValueError):
        ticket_price(age)


# EP – klasy niepoprawne (typ): BL-4
@pytest.mark.parametrize("age", [
    pytest.param(30.5, id="float"),
    pytest.param("30", id="str"),
    pytest.param(None, id="none"),
    pytest.param(True, id="bool"),
])
def test_ep_wrong_type(age):
    with pytest.raises(TypeError):
        ticket_price(age)


# AWB 2-punktowa: wartości w dziedzinie (0-120)
@pytest.mark.parametrize("age, price", [
    pytest.param(0, 0.0, id="0"),
    pytest.param(6, 0.0, id="6"),
    pytest.param(7, 10.0, id="7"),
    pytest.param(18, 10.0, id="18"),
    pytest.param(19, 20.0, id="19"),
    pytest.param(64, 20.0, id="64"),
    pytest.param(65, 10.0, id="65"),
    pytest.param(120, 10.0, id="120",
                 marks=pytest.mark.xfail(reason="DEF-05", strict=True)),
])
def test_bva_2p(age, price):
    assert ticket_price(age) == price


# AWB 2-punktowa: wartości poza dziedziną
@pytest.mark.parametrize("age", [
    pytest.param(-1, id="-1"),
    pytest.param(121, id="121"),
])
def test_bva_2p_out_of_domain(age):
    with pytest.raises(ValueError):
        ticket_price(age)


# AWB 3-punktowa: tylko wartości dokładane do 2p
@pytest.mark.parametrize("age, price", [
    pytest.param(1, 0.0, id="1"),
    pytest.param(5, 0.0, id="5"),
    pytest.param(8, 10.0, id="8"),
    pytest.param(17, 10.0, id="17"),
    pytest.param(20, 20.0, id="20"),
    pytest.param(63, 20.0, id="63"),
    pytest.param(66, 10.0, id="66"),
    pytest.param(119, 10.0, id="119",
                 marks=pytest.mark.xfail(reason="DEF-05", strict=True)),
])
def test_bva_3p_extra(age, price):
    assert ticket_price(age) == price