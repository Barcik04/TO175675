"""Moduły testowane na ćwiczeniach 2 (testy czarnoskrzynkowe).

Testy projektujemy WYŁĄCZNIE na podstawie pliku SPECYFIKACJA.md.
Nie czytaj kodu w tym katalogu przed zakończeniem ćwiczenia.
"""
from .passwords import validate_password
from .grades import grade_from_percent
from .parking import parking_fee
from .tickets import ticket_price

__all__ = ["grade_from_percent", "parking_fee",
           "validate_password", "ticket_price"]
