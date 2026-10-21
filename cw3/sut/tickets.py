"""Cena biletu do muzeum zależna od wieku zwiedzającego."""

MAX_AGE = 100        # najstarszy obsługiwany wiek

FREE_PRICE = 0.0     # dzieci do 6 lat
REDUCED_PRICE = 10.0 # dzieci i młodzież 7-18 lat oraz seniorzy 65+
NORMAL_PRICE = 20.0  # pozostali (19-64 lata)


def ticket_price(age):
    """Zwraca cenę biletu w zł dla zwiedzającego w wieku `age` lat.

    Wymagania: SPECYFIKACJA.md, punkty BL-1 ... BL-4.
    """
    if isinstance(age, bool) or not isinstance(age, int):
        raise TypeError("wiek musi być liczbą całkowitą (int)")
    if age < 0 or age > MAX_AGE:
        raise ValueError("wiek spoza obsługiwanego zakresu")
    if age <= 6:
        return FREE_PRICE
    if age <= 18:
        return REDUCED_PRICE
    if age < 65:
        return NORMAL_PRICE
    return REDUCED_PRICE
