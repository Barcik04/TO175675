# Specyfikacja modułu `sut` (ćwiczenia 2)

Pakiet `sut` udostępnia cztery funkcje. Testy projektujemy **wyłącznie na podstawie
tego dokumentu** (testowanie czarnoskrzynkowe) – nie zaglądamy do kodu źródłowego.

```python
from sut import grade_from_percent, parking_fee, validate_password, ticket_price
```

---

## 1. `grade_from_percent(percent)` – ocena z przedmiotu

Funkcja wyznacza ocenę końcową na podstawie procentu zdobytych punktów
(progi z regulaminu przedmiotu).

| ID   | Wymaganie |
|------|-----------|
| OC-1 | Argument `percent` to liczba całkowita typu `int` z zakresu 0–100 (włącznie). |
| OC-2 | Funkcja zwraca ocenę jako liczbę typu `float` zgodnie z tabelą progów poniżej. |
| OC-3 | Dla wartości typu `int` spoza zakresu 0–100 funkcja zgłasza wyjątek `ValueError`. |
| OC-4 | Dla argumentu innego typu niż `int` (np. `float`, `str`, `None`, `bool`) funkcja zgłasza wyjątek `TypeError`. Wartość nie jest zaokrąglana ani konwertowana. |

| Procent punktów | Ocena | Zwracana wartość |
|-----------------|-------|------------------|
| 0–50            | niedostateczny | `2.0` |
| 51–60           | dostateczny | `3.0` |
| 61–70           | dostateczny plus | `3.5` |
| 71–80           | dobry | `4.0` |
| 81–90           | dobry plus | `4.5` |
| 91–100          | bardzo dobry | `5.0` |

Przykład: `grade_from_percent(75)` → `4.0`.

---

## 2. `parking_fee(minutes)` – opłata za parking

Funkcja oblicza opłatę (w złotych) za jednorazowy postój na parkingu uczelnianym.

| ID   | Wymaganie |
|------|-----------|
| PK-1 | Argument `minutes` to czas postoju w pełnych minutach: liczba całkowita typu `int` z zakresu 0–1440 (maks. jedna doba). |
| PK-2 | Postój trwający od 0 do 15 minut (włącznie) jest bezpłatny – opłata `0.0`. |
| PK-3 | Postój od 16 do 180 minut: 5,00 zł za każdą **rozpoczętą** godzinę postoju, licząc od początku postoju (np. 16 min → `5.0`, 61 min → `10.0`). |
| PK-4 | Postój dłuższy niż 180 minut (181–1440): stała opłata dobowa `20.0`. |
| PK-5 | Wartość typu `int` spoza zakresu 0–1440 → `ValueError`; argument innego typu niż `int` (np. `float`, `str`, `bool`) → `TypeError`. |

Przykład: `parking_fee(150)` → `15.0` (rozpoczęte 3 godziny).

---

## 3. `validate_password(password)` – walidacja hasła

Funkcja sprawdza, czy hasło podane przy zakładaniu konta spełnia reguły.

| ID   | Wymaganie |
|------|-----------|
| HS-1 | Argument `password` jest napisem (`str`). Argument innego typu → `TypeError`. |
| HS-2 | Hasło ma długość od 8 do 20 znaków (włącznie). |
| HS-3 | Hasło zawiera co najmniej jedną literę (dowolną, także polską, np. `ą`, `Ż`) i co najmniej jedną cyfrę. |
| HS-4 | Poza tym hasło może zawierać **dowolne** znaki, w tym znaki specjalne (np. `#`, `!`, `@`) i spacje. |

Funkcja zwraca `True`, gdy spełnione są HS-2 i HS-3 (przy HS-4), a w przeciwnym razie `False`.

Przykład: `validate_password("haslo123")` → `True`, `validate_password("haslo")` → `False`.

---

## 4. `ticket_price(age)` – cena biletu do muzeum

Funkcja wyznacza cenę (w złotych) jednorazowego biletu wstępu do muzeum
na podstawie wieku zwiedzającego.

| ID   | Wymaganie |
|------|-----------|
| BL-1 | Argument `age` to wiek zwiedzającego w pełnych latach: liczba całkowita typu `int` z zakresu 0–120 (włącznie). |
| BL-2 | Funkcja zwraca cenę biletu jako liczbę typu `float` zgodnie z tabelą cen poniżej. |
| BL-3 | Dla wartości typu `int` spoza zakresu 0–120 funkcja zgłasza wyjątek `ValueError`. |
| BL-4 | Dla argumentu innego typu niż `int` (np. `float`, `str`, `None`, `bool`) funkcja zgłasza wyjątek `TypeError`. |

| Wiek (lata) | Rodzaj biletu | Zwracana wartość |
|-------------|---------------|------------------|
| 0–6         | bezpłatny | `0.0` |
| 7–18        | ulgowy (dzieci i młodzież) | `10.0` |
| 19–64       | normalny | `20.0` |
| 65–120      | ulgowy (seniorzy) | `10.0` |

Przykład: `ticket_price(30)` → `20.0`, `ticket_price(70)` → `10.0`.
