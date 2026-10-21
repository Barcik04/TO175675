"""Pierwsze testy – sprawdzenie, czy pytest działa w projekcie."""


def add(a, b):
    return a + b


def test_add_integers():
    assert add(2, 3) == 5


def test_add_floats():
    # Ten test celowo NIE przechodzi – przeczytaj raport pytest!
    assert add(0.1, 0.2) == 0.3
