"""Adresy stron używanych na ćwiczeniach.

Domyślnie testy korzystają z publicznych stron i lokalnego XAMPP.
Każdy adres można nadpisać zmienną środowiskową (np. w PyCharm: Run > Edit Configurations > Environment variables).
"""
import os

INTERNET_URL = os.getenv("INTERNET_URL", "https://the-internet.herokuapp.com").rstrip("/")
SELENIUM_WEB_URL = os.getenv("SELENIUM_WEB_URL", "https://www.selenium.dev/selenium/web").rstrip("/")
SKLEPTO_URL = os.getenv("SKLEPTO_URL", "http://localhost/sklepto").rstrip("/")
