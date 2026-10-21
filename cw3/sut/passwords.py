"""Walidacja hasła przy zakładaniu konta."""

MIN_LEN = 8
MAX_LEN = 20


def validate_password(password):
    """Zwraca True, gdy hasło spełnia reguły, a w innym razie False.

    Wymagania: SPECYFIKACJA.md, punkty HS-1 ... HS-4.
    """
    if not isinstance(password, str):
        raise TypeError("hasło musi być napisem (str)")
    if len(password) < MIN_LEN or len(password) > MAX_LEN:
        return False
    if not password.isalnum():
        return False
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_letter and has_digit
