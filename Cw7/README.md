# Ćwiczenia 7 – pliki startowe (część B)

Wymagania: działający XAMPP (Apache + MySQL) i SklepTO pod adresem `http://localhost/sklepto`. Inny port? Ustaw zmienną `SKLEPTO_URL`, np. `http://localhost:8080/sklepto`.

1. Skopiuj zawartość tego katalogu do projektu 
2. `pip install -r requirements.txt` (plik z katalogu `wspolne` materiałów kursu).
3. `pytest -v` – na starcie część testów przechodzi, reszta ma status `SKIPPED` (TODO).

| Plik | Zawartość |
|---|---|
| `konfiguracja.py` | adresy (zmienna `SKLEPTO_URL`) |
| `conftest.py` | fixture `driver`; w kroku B3 dopiszesz reset bazy |
| `formularz.py` | wypełnianie formularza i odczyt komunikatów (gotowe) |
| `tabele.md` | tabele EP i AWB – uzupełnij **przed** pisaniem testów |
| `test_rejestracja_ep.py` | testy klas równoważności |
| `test_rejestracja_awb.py` | testy wartości brzegowych 2p i 3p |
| `test_rejestracja_dane.py` | testy z plików `dane/*.csv` (i `*.json`) |
| `raport_defektu.md` | szablon raportu defektu |
