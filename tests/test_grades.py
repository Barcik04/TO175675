"""Testy czarnoskrzynkowe: grade_from_percent (OC-1 ... OC-4)."""
import pytest

from sut import grade_from_percent


# EP – klasy poprawne: jedna typowa wartość z każdej klasy
@pytest.mark.parametrize("percent, grade", [
    pytest.param(25, 2.0, id="fail"),
    pytest.param(55, 3.0, id="satisfactory"),
    pytest.param(65, 3.5, id="satisfactory_plus"),
    pytest.param(75, 4.0, id="good"),
    pytest.param(85, 4.5, id="good_plus"),
    pytest.param(95, 5.0, id="very_good"),
])
def test_ep_valid_classes(percent, grade):
    assert grade_from_percent(percent) == grade


# EP – klasy niepoprawne (wartość): jeden test = jedna klasa
@pytest.mark.parametrize("percent", [
    pytest.param(-10, id="negative"),
    pytest.param(150, id="above_100"),
])
def test_ep_out_of_range(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)


# EP – klasy niepoprawne (typ): OC-4
@pytest.mark.parametrize("percent", [
    pytest.param(75.5, id="float",
                 marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
    pytest.param("75", id="str",
                 marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
    pytest.param(None, id="none"),
    pytest.param(True, id="bool",
                 marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
])
def test_ep_wrong_type(percent):
    with pytest.raises(TypeError):
        grade_from_percent(percent)


# AWB 2-punktowa: wartości w dziedzinie (0-100)
@pytest.mark.parametrize("percent, grade", [
    pytest.param(0, 2.0, id="0"),
    pytest.param(50, 2.0, id="50"),
    pytest.param(51, 3.0, id="51"),
    pytest.param(60, 3.0, id="60"),
    pytest.param(61, 3.5, id="61"),
    pytest.param(70, 3.5, id="70"),
    pytest.param(71, 4.0, id="71"),
    pytest.param(80, 4.0, id="80"),
    pytest.param(81, 4.5, id="81"),
    pytest.param(90, 4.5, id="90",
                 marks=pytest.mark.xfail(reason="DEF-02", strict=True)),
    pytest.param(91, 5.0, id="91"),
    pytest.param(100, 5.0, id="100"),
])
def test_bva_2p(percent, grade):
    assert grade_from_percent(percent) == grade


# AWB 2-punktowa: wartości poza dziedziną
@pytest.mark.parametrize("percent", [
    pytest.param(-1, id="-1"),
    pytest.param(101, id="101"),
])
def test_bva_2p_out_of_domain(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)


# AWB 3-punktowa: tylko wartości dokładane do 2p
@pytest.mark.parametrize("percent, grade", [
    pytest.param(1, 2.0, id="1"),
    pytest.param(49, 2.0, id="49"),
    pytest.param(52, 3.0, id="52"),
    pytest.param(59, 3.0, id="59"),
    pytest.param(62, 3.5, id="62"),
    pytest.param(69, 3.5, id="69"),
    pytest.param(72, 4.0, id="72"),
    pytest.param(79, 4.0, id="79"),
    pytest.param(82, 4.5, id="82"),
    pytest.param(89, 4.5, id="89"),
    pytest.param(92, 5.0, id="92"),
    pytest.param(99, 5.0, id="99"),
])
def test_bva_3p_extra(percent, grade):
    assert grade_from_percent(percent) == grade