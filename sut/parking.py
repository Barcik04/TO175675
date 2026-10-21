"""Opłata za postój na parkingu uczelnianym."""
import math

FREE_MINUTES = 15   # tyle minut postoju nic nie kosztuje
HOURLY_LIMIT = 180  # do tylu minut liczy się stawkę godzinową
HOURLY_RATE = 5.0   # zł za każdą rozpoczętą godzinę
DAILY_FEE = 20.0    # zł za postój dłuższy niż 180 minut
MAX_MINUTES = 1440  # jedna doba


def parking_fee(minutes):
    """Zwraca opłatę w zł za postój trwający `minutes` minut.

    Wymagania: SPECYFIKACJA.md, punkty PK-1 ... PK-5.
    """
    if isinstance(minutes, bool) or not isinstance(minutes, int):
        raise TypeError("czas postoju musi być liczbą całkowitą")
    if minutes < 0 or minutes > MAX_MINUTES:
        raise ValueError("czas postoju musi być z zakresu 0-1440")
    if minutes == 0:
        return 0.0                      # brak postoju
    if 1 < minutes <= FREE_MINUTES:
        return 0.0                      # czas bezpłatny
    if minutes > HOURLY_LIMIT:
        return DAILY_FEE
    hours = math.ceil(minutes / 60)
    return HOURLY_RATE * hours
