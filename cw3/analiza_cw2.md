# Analiza – ćwiczenie 2: klasy równoważności

## 1. grade_from_percent

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
|-------|------|--------|---------|------------|
| OC-K1 | 0–50 | poprawna | 25 | `2.0` |
| OC-K2 | 51–60 | poprawna | 55 | `3.0` |
| OC-K3 | 61–70 | poprawna | 65 | `3.5` |
| OC-K4 | 71–80 | poprawna | 75 | `4.0` |
| OC-K5 | 81–90 | poprawna | 85 | `4.5` |
| OC-K6 | 91–100 | poprawna | 95 | `5.0` |
| OC-N1 | < 0 | niepoprawna (wartość) | -10 | `ValueError` |
| OC-N2 | > 100 | niepoprawna (wartość) | 150 | `ValueError` |
| OC-N3 | typ float | niepoprawna (typ) | 75.5 | `TypeError` |
| OC-N4 | typ str | niepoprawna (typ) | "75" | `TypeError` |
| OC-N5 | typ None | niepoprawna (typ) | None | `TypeError` |
| OC-N6 | typ bool | niepoprawna (typ) | True | `TypeError` |

## 2. parking_fee

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
|-------|------|--------|---------|------------|
| PK-K1 | 0–15 min (wyjście 0 zł) | poprawna | 10 | `0.0` |
| PK-K2 | 16–60 min (wyjście 5 zł) | poprawna | 40 | `5.0` |
| PK-K3 | 61–120 min (wyjście 10 zł) | poprawna | 90 | `10.0` |
| PK-K4 | 121–180 min (wyjście 15 zł) | poprawna | 150 | `15.0` |
| PK-K5 | 181–1440 min (wyjście 20 zł) | poprawna | 600 | `20.0` |
| PK-N1 | < 0 | niepoprawna (wartość) | -5 | `ValueError` |
| PK-N2 | > 1440 | niepoprawna (wartość) | 2000 | `ValueError` |
| PK-N3 | typ float | niepoprawna (typ) | 30.5 | `TypeError` |
| PK-N4 | typ str | niepoprawna (typ) | "30" | `TypeError` |
| PK-N5 | typ bool | niepoprawna (typ) | True | `TypeError` |

## 3. validate_password

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
|-------|------|--------|---------|------------|
| HS-K1 | długość 8–20, litery + cyfry | poprawna | `haslo123` | `True` |
| HS-K2 | znaki specjalne | poprawna | `haslo#123!` | `True` |
| HS-K3 | spacje | poprawna | `has lo 123` | `True` |
| HS-K4 | polskie litery | poprawna | `Żółw1234` | `True` |
| HS-N1 | długość < 8 | niepoprawna (długość) | `ha1` | `False` |
| HS-N2 | długość > 20 | niepoprawna (długość) | `a1` × 11 (22 znaki) | `False` |
| HS-N3 | brak cyfry | niepoprawna (skład) | `haslohaslo` | `False` |
| HS-N4 | brak litery | niepoprawna (skład) | `12345678` | `False` |
| HS-N5 | typ None | niepoprawna (typ) | None | `TypeError` |
| HS-N6 | typ int | niepoprawna (typ) | 12345678 | `TypeError` |

## 4. ticket_price

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
|-------|------|--------|---------|------------|
| BL-K1 | 0–6 lat (bezpłatny, wyjście 0 zł) | poprawna | 3 | `0.0` |
| BL-K2 | 7–18 lat (ulgowy, wyjście 10 zł) | poprawna | 12 | `10.0` |
| BL-K3 | 19–64 lata (normalny, wyjście 20 zł) | poprawna | 40 | `20.0` |
| BL-K4 | 65–120 lat (senior, wyjście 10 zł) | poprawna | 70 | `10.0` |
| BL-N1 | < 0 | niepoprawna (wartość) | -1 | `ValueError` |
| BL-N2 | > 120 | niepoprawna (wartość) | 150 | `ValueError` |
| BL-N3 | typ float | niepoprawna (typ) | 30.5 | `TypeError` |
| BL-N4 | typ str | niepoprawna (typ) | "30" | `TypeError` |
| BL-N5 | typ None | niepoprawna (typ) | None | `TypeError` |
| BL-N6 | typ bool | niepoprawna (typ) | True | `TypeError` |










# Analiza – ćwiczenie 2: wartości brzegowe (AWB)

Precyzja: 1 (punkt procentowy / minuta / znak / rok).

## 1. grade_from_percent (precyzja: 1 punkt procentowy)

| Granica | 2p | 3p – dodatkowo | Oczekiwane |
|---------|----|----------------|------------|
| -1 \| 0 | -1, 0 | 1 | -1 → `ValueError`; 0, 1 → `2.0` |
| 50 \| 51 | 50, 51 | 49, 52 | 49, 50 → `2.0`; 51, 52 → `3.0` |
| 60 \| 61 | 60, 61 | 59, 62 | 59, 60 → `3.0`; 61, 62 → `3.5` |
| 70 \| 71 | 70, 71 | 69, 72 | 69, 70 → `3.5`; 71, 72 → `4.0` |
| 80 \| 81 | 80, 81 | 79, 82 | 79, 80 → `4.0`; 81, 82 → `4.5` |
| 90 \| 91 | 90, 91 | 89, 92 | 89, 90 → `4.5`; 91, 92 → `5.0` |
| 100 \| 101 | 100, 101 | 99 | 99, 100 → `5.0`; 101 → `ValueError` |

Pokrycie: 2p = 14 elementów, 3p = 14 + 12 = 26.

## 2. parking_fee (precyzja: 1 minuta)

| Granica | 2p | 3p – dodatkowo | Oczekiwane |
|---------|----|----------------|------------|
| -1 \| 0 | -1, 0 | 1 | -1 → `ValueError`; 0, 1 → `0.0` |
| 15 \| 16 | 15, 16 | 14, 17 | 14, 15 → `0.0`; 16, 17 → `5.0` |
| 60 \| 61 | 60, 61 | 59, 62 | 59, 60 → `5.0`; 61, 62 → `10.0` |
| 120 \| 121 | 120, 121 | 119, 122 | 119, 120 → `10.0`; 121, 122 → `15.0` |
| 180 \| 181 | 180, 181 | 179, 182 | 179, 180 → `15.0`; 181, 182 → `20.0` |
| 1440 \| 1441 | 1440, 1441 | 1439 | 1439, 1440 → `20.0`; 1441 → `ValueError` |

Pokrycie: 2p = 12 elementów, 3p = 12 + 10 = 22.

## 3. validate_password (precyzja: 1 znak długości)

Hasła o danej długości generuje `password_of_length(n)`.

| Granica | 2p | 3p – dodatkowo | Oczekiwane |
|---------|----|----------------|------------|
| 7 \| 8 | 7, 8 | 6, 9 | 6, 7 → `False`; 8, 9 → `True` |
| 20 \| 21 | 20, 21 | 19, 22 | 19, 20 → `True`; 21, 22 → `False` |

Klasa „krótsze niż 8" i klasa „dłuższe niż 20" są otwarte, więc każda ma jeden brzeg.
Klasy składu (litera, cyfra, znaki specjalne) nie mają uporządkowanej osi liczbowej, więc nie podlegają AWB.

Pokrycie: 2p = 4 elementy, 3p = 4 + 4 = 8.

## 4. ticket_price (precyzja: 1 rok)

| Granica | 2p | 3p – dodatkowo | Oczekiwane |
|---------|----|----------------|------------|
| -1 \| 0 | -1, 0 | 1 | -1 → `ValueError`; 0, 1 → `0.0` |
| 6 \| 7 | 6, 7 | 5, 8 | 5, 6 → `0.0`; 7, 8 → `10.0` |
| 18 \| 19 | 18, 19 | 17, 20 | 17, 18 → `10.0`; 19, 20 → `20.0` |
| 64 \| 65 | 64, 65 | 63, 66 | 63, 64 → `20.0`; 65, 66 → `10.0` |
| 120 \| 121 | 120, 121 | 119 | 119, 120 → `10.0`; 121 → `ValueError` |

Pokrycie: 2p = 10 elementów, 3p = 10 + 8 = 18.

## Podsumowanie pokrycia

| Funkcja | 2p | 3p (łącznie) |
|---------|----|--------------|
| grade_from_percent | 14 | 26 |
| parking_fee | 12 | 22 |
| validate_password | 4 | 8 |
| ticket_price | 10 | 18 |
| **Razem** | **40** | **74** |





## Wyniki: lista nieudanych testów

Polecenie: `python -m pytest -v`, drugi raz `python -m pytest --lf -v` (te same porażki).

| Test | Wymaganie | Wynik otrzymany | Wynik oczekiwany |
|------|-----------|-----------------|------------------|
| test_grades.py::test_ep_wrong_type[float] | OC-4 | brak wyjątku | `TypeError` |
| test_grades.py::test_ep_wrong_type[str] | OC-4 | brak wyjątku | `TypeError` |
| test_grades.py::test_ep_wrong_type[bool] | OC-4 | brak wyjątku | `TypeError` |
| test_grades.py::test_bva_2p[90] | OC-2 | `5.0` | `4.5` |
| test_parking.py::test_bva_3p_extra[1] | PK-2 | `5.0` | `0.0` |
| test_passwords.py::test_ep_valid[special_chars] | HS-4 | `False` | `True` |
| test_passwords.py::test_ep_valid[spaces] | HS-4 | `False` | `True` |
| test_tickets.py::test_bva_2p[120] | BL-1 | `ValueError` | `10.0` |
| test_tickets.py::test_bva_3p_extra[119] | BL-1 | `ValueError` | `10.0` |
| test_first.py::test_add_floats | (test przykładowy, spoza `sut`) | `0.30000000000000004` | `0.3` |

Uwaga: `test_first.py::test_add_floats` jest celowo czerwony i nie dotyczy modułu `sut`.

10 nieudanych testów, w tym 1 przykładowy (test_add_floats); 9 testów modułu sut wykrywa 5 defektów






## B9. Analiza porażek


| Defekt | Test(y) | Oczekiwane vs otrzymane | Zgodne ze spec? | Rozstrzygnięcie | Wykryła technika | Czy inna technika by wykryła? |
|--------|---------|-------------------------|-----------------|-----------------|------------------|-------------------------------|
| D1: brak kontroli typu (OC-4) | `test_grades::test_ep_wrong_type[float]`, `[str]`, `[bool]` | `TypeError` vs DID NOT RAISE | tak (OC-4) | defekt w `sut` | EP (klasy niepoprawne typu) | Nie. Testy AWB używają tylko `int`. |
| D2: próg 4.5/5.0 przesunięty (OC-2) | `test_grades::test_bva_2p[90]` | `4.5` vs `5.0` | tak (81–90 → 4.5) | defekt w `sut` | AWB 2p (granica 90\|91) | Nie przez EP: wartości 85 i 95 przeszły. 3p_extra (89, 92) też nie, bo błąd jest tylko w 90. |
| D3: 1 minuta płatna (PK-2) | `test_parking::test_bva_3p_extra[1]` | `0.0` vs `5.0` | tak (0–15 min bezpłatne) | defekt w `sut` | AWB 3p (sąsiad brzegu 0) | Nie przez 2p (0 i 15 przeszły) ani EP (reprezentant 10 przeszedł). EP wykryłoby to tylko przypadkiem, gdyby reprezentantem było 1. |
| D4: znaki specjalne i spacje odrzucane (HS-4) | `test_passwords::test_ep_valid[special_chars]`, `[spaces]` | `True` vs `False` | tak (HS-4: dowolne znaki) | defekt w `sut` | EP (osobne klasy dla HS-4) | Nie. AWB długości używa `password_of_length` (same litery i cyfry). |
| D5: górna granica wieku 100 zamiast 120 (BL-1) | `test_tickets::test_bva_2p[120]`, `test_bva_3p_extra[119]` | `10.0` vs `ValueError` | tak (BL-1: 0–120) | defekt w `sut` | AWB 2p (brzeg dziedziny 120); 119 to ten sam defekt w 3p | Nie przez EP: reprezentant 70 przeszedł. Brzeg 121 → `ValueError` też przeszedł. |

### Wnioski
- 9 czerwonych testów `sut` = 5 defektów (D1 x3, D2 x1, D3 x1, D4 x2, D5 x2).
- Każda technika wykryła coś, czego inne nie wykryły: EP (D1, D4), AWB 2p (D2, D5), AWB 3p (D3).
- EP z jedną wartością na klasę przeoczyło D2, D3 i D5, bo błędy leżą na granicach lub tuż przy nich.
- 3p wykryło dodatkowo tylko D3. W D5 wartość 119 nie dodaje nowego defektu, bo 120 z 2p już go wykrywa.





# Defekty

## DEF-01: `grade_from_percent(x)` nie zgłasza TypeError dla argumentów float, str i bool

| Pole | Treść |
|------|-------|
| Wymaganie | OC-4 |
| Kroki | Wywołać `grade_from_percent(75.5)`, `grade_from_percent("75")`, `grade_from_percent(True)` |
| Oczekiwany (spec.) | `TypeError`, wartość nie jest zaokrąglana ani konwertowana |
| Rzeczywisty (pytest) | `DID NOT RAISE TypeError` (funkcja konwertuje argument na `int`) |
| Test | `test_grades.py::test_ep_wrong_type[float]`, `[str]`, `[bool]` |
| Ważność | wysoka |

## DEF-02: `grade_from_percent(90)` zwraca 5.0 zamiast 4.5

| Pole | Treść |
|------|-------|
| Wymaganie | OC-2 (tabela progów: 81–90 → 4.5) |
| Kroki | Wywołać `grade_from_percent(90)` |
| Oczekiwany (spec.) | `4.5` |
| Rzeczywisty (pytest) | `5.0` (`assert 5.0 == 4.5`) |
| Test | `test_grades.py::test_bva_2p[90]` |
| Ważność | wysoka (zła ocena końcowa) |

## DEF-03: `parking_fee(1)` zwraca 5.0 zamiast 0.0

| Pole | Treść |
|------|-------|
| Wymaganie | PK-2 (postój 0–15 min jest bezpłatny) |
| Kroki | Wywołać `parking_fee(1)` |
| Oczekiwany (spec.) | `0.0` |
| Rzeczywisty (pytest) | `5.0` (`assert 5.0 == 0.0`) |
| Test | `test_parking.py::test_bva_3p_extra[1]` |
| Ważność | średnia (dotyczy jednej wartości, ale kierowca płaci bez podstawy) |

## DEF-04: `validate_password` zwraca False dla haseł ze znakami specjalnymi i spacjami

| Pole | Treść |
|------|-------|
| Wymaganie | HS-4 (poza literą i cyfrą hasło może zawierać dowolne znaki) |
| Kroki | Wywołać `validate_password("haslo#123!")` oraz `validate_password("has lo 123")` |
| Oczekiwany (spec.) | `True` (długość 8–20, zawiera literę i cyfrę) |
| Rzeczywisty (pytest) | `False` (`assert False is True`) |
| Test | `test_passwords.py::test_ep_valid[special_chars]`, `[spaces]` |
| Ważność | wysoka (poprawne hasła są odrzucane, użytkownik nie założy konta) |

## DEF-05: `ticket_price(x)` zgłasza ValueError dla wieku powyżej 100

| Pole | Treść |
|------|-------|
| Wymaganie | BL-1 (wiek 0–120 włącznie), BL-2 (65–120 → 10.0) |
| Kroki | Wywołać `ticket_price(120)` oraz `ticket_price(119)` |
| Oczekiwany (spec.) | `10.0` |
| Rzeczywisty (pytest) | `ValueError: wiek spoza obsługiwanego zakresu` |
| Test | `test_tickets.py::test_bva_2p[120]`, `test_bva_3p_extra[119]` |
| Ważność | średnia (dotyczy tylko wieku 101–120) |






## Zadania Samodzielne

| Funkcja | Klasy EP (pokryte / wszystkie) | AWB 2p | AWB 3p (łącznie) |
|---------|-------------------------------|--------|------------------|
| grade_from_percent | 12 / 12 | 14 / 14 | 26 / 26 |
| parking_fee | 10 / 10 | 12 / 12 | 22 / 22 |
| validate_password | 10 / 10 | 4 / 4 | 8 / 8 |
| ticket_price | 10 / 10 | 10 / 10 | 18 / 18 |
| **Razem** | **42 / 42 (100%)** | **40 / 40 (100%)** | **74 / 74 (100%)** |


### Hasło 20-znakowe z polskimi literami
Hasło: `Żółćgęśląjaźń1234567` (13 liter + 7 cyfr = 20 znaków)
Oczekiwany wynik (spec.: HS-2, HS-3): `True`
Wynik rzeczywisty: (wpisz to, co zwróci polecenie)

### Each Choice dla validate_password

| # | Hasło | Pokrywane klasy | Oczekiwany |
|---|-------|-----------------|------------|
| 1 | `Żółw#1234!` | litery + cyfry, polskie litery, znaki specjalne | `True` |
| 2 | `has lo 123` | spacje | `True` |
| 3 | `ha1` | za krótkie | `False` |
| 4 | `a1` × 11 | za długie | `False` |
| 5 | `haslohaslo` | brak cyfry | `False` |
| 6 | `12345678` | brak litery | `False` |
| 7 | `None` | typ ≠ str | `TypeError` |
| 8 | `12345678` (int) | typ ≠ str | `TypeError` |

Razem 8 przypadków zamiast 10 klas z EP: trzy klasy poprawne (litery i cyfry, polskie litery, znaki specjalne) są pokryte jednym hasłem. Klasy niepoprawne sprawdzam osobno, żeby jeden błąd nie maskował drugiego.

# python -c "from sut import validate_password; print(validate_password('Żółćgęśląjaźń1234567'))"
### wynik TRUE


#
#
#
# Porównaj wykryte defekty z techniką, która je znalazła (EP / AWB 2p / 3p) – czy któraś technika wystarczyłaby sama?
### żadna. EP wykryło D1 i D4, AWB 2p wykryło D2 i D5, a AWB 3p wykryło D3, którego pozostałe nie złapały.



#
#
#
#
## raport html wygenerowany jest w tym samym folderze co analizwa_cw2.md