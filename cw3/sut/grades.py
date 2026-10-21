"""Ocena z przedmiotu na podstawie procentu zdobytych punktów."""


def grade_from_percent(percent):
    """Zwraca ocenę (float) dla procentu punktów 0-100.

    Wymagania: SPECYFIKACJA.md, punkty OC-1 ... OC-4.
    """
    percent = int(percent)
    if percent < 0 or percent > 100:
        raise ValueError("procent musi być z zakresu 0-100")
    if percent >= 90:
        return 5.0
    if percent > 80:
        return 4.5
    if percent > 70:
        return 4.0
    if percent > 60:
        return 3.5
    if percent > 50:
        return 3.0
    return 2.0
