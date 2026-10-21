"""Testy czarnoskrzynkowe: parking_fee (PK-1 ... PK-5)."""
import pytest

from sut import parking_fee


# EP – klasy poprawne (także klasy WYJŚĆ: 0 zł, 5 zł, 10 zł, 15 zł, 20 zł)
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(10, 0.0, id="free"),
    pytest.param(40, 5.0, id="1h"),
    pytest.param(90, 10.0, id="2h"),
    pytest.param(150, 15.0, id="3h"),
    pytest.param(600, 20.0, id="daily"),
])
def test_ep_valid_classes(minutes, fee):
    assert parking_fee(minutes) == fee


# EP – klasy niepoprawne (wartość): jeden test = jedna klasa
@pytest.mark.parametrize("minutes", [
    pytest.param(-5, id="negative"),
    pytest.param(2000, id="above_1440"),
])
def test_ep_out_of_range(minutes):
    with pytest.raises(ValueError):
        parking_fee(minutes)


# EP – klasy niepoprawne (typ): PK-5
@pytest.mark.parametrize("minutes", [
    pytest.param(30.5, id="float"),
    pytest.param("30", id="str"),
    pytest.param(True, id="bool"),
])
def test_ep_wrong_type(minutes):
    with pytest.raises(TypeError):
        parking_fee(minutes)


# AWB 2-punktowa: wartości w dziedzinie (0-1440)
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(0, 0.0, id="0"),
    pytest.param(15, 0.0, id="15"),
    pytest.param(16, 5.0, id="16"),
    pytest.param(60, 5.0, id="60"),
    pytest.param(61, 10.0, id="61"),
    pytest.param(120, 10.0, id="120"),
    pytest.param(121, 15.0, id="121"),
    pytest.param(180, 15.0, id="180"),
    pytest.param(181, 20.0, id="181"),
    pytest.param(1440, 20.0, id="1440"),
])
def test_bva_2p(minutes, fee):
    assert parking_fee(minutes) == fee


# AWB 2-punktowa: wartości poza dziedziną
@pytest.mark.parametrize("minutes", [
    pytest.param(-1, id="-1"),
    pytest.param(1441, id="1441"),
])
def test_bva_2p_out_of_domain(minutes):
    with pytest.raises(ValueError):
        parking_fee(minutes)


# AWB 3-punktowa: tylko wartości dokładane do 2p
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(1, 0.0, id="1",
                 marks=pytest.mark.xfail(reason="DEF-03", strict=True)),
    pytest.param(14, 0.0, id="14"),
    pytest.param(17, 5.0, id="17"),
    pytest.param(59, 5.0, id="59"),
    pytest.param(62, 10.0, id="62"),
    pytest.param(119, 10.0, id="119"),
    pytest.param(122, 15.0, id="122"),
    pytest.param(179, 15.0, id="179"),
    pytest.param(182, 20.0, id="182"),
    pytest.param(1439, 20.0, id="1439"),
])
def test_bva_3p_extra(minutes, fee):
    assert parking_fee(minutes) == fee