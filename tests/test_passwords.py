"""Testy czarnoskrzynkowe: validate_password (HS-1 ... HS-4)."""
import pytest

from sut import validate_password


def password_of_length(n):
    """Hasło z liter i cyfr o długości n, np. 5 -> 'a1a1a'."""
    return ("a1" * n)[:n]


def test_example_valid_password():
    assert validate_password("haslo123") is True


def test_example_wrong_type():
    with pytest.raises(TypeError):
        validate_password(None)


# EP – klasy poprawne (HS-3, HS-4)
@pytest.mark.parametrize("password", [
    pytest.param("haslo123", id="letters_digits"),
    pytest.param("haslo#123!", id="special_chars",
                 marks=pytest.mark.xfail(reason="DEF-04", strict=True)),
    pytest.param("has lo 123", id="spaces",
                 marks=pytest.mark.xfail(reason="DEF-04", strict=True)),
    pytest.param("Żółw1234", id="polish_letters"),
])
def test_ep_valid(password):
    assert validate_password(password) is True


# EP – klasy niepoprawne: każda osobno
@pytest.mark.parametrize("password", [
    pytest.param("ha1", id="too_short"),
    pytest.param("a1" * 11, id="too_long"),
    pytest.param("haslohaslo", id="no_digit"),
    pytest.param("12345678", id="no_letter"),
])
def test_ep_invalid(password):
    assert validate_password(password) is False


# EP – klasa niepoprawna (typ): HS-1
def test_ep_wrong_type_int():
    with pytest.raises(TypeError):
        validate_password(12345678)


# AWB długości, 2-punktowa: 7|8 i 20|21
@pytest.mark.parametrize("n, expected", [
    pytest.param(7, False, id="7"),
    pytest.param(8, True, id="8"),
    pytest.param(20, True, id="20"),
    pytest.param(21, False, id="21"),
])
def test_bva_length_2p(n, expected):
    assert validate_password(password_of_length(n)) is expected


# AWB długości, 3-punktowa: tylko wartości dokładane do 2p
@pytest.mark.parametrize("n, expected", [
    pytest.param(6, False, id="6"),
    pytest.param(9, True, id="9"),
    pytest.param(19, True, id="19"),
    pytest.param(22, False, id="22"),
])
def test_bva_length_3p_extra(n, expected):
    assert validate_password(password_of_length(n)) is expected