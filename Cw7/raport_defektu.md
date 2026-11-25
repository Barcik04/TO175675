# Raport defektu

| Pole | Wartość |
|---|---|
| Identyfikator | DEF-REJ-01 |
| Tytuł | Rejestracja (rejestracja.php): wiek 100 jest przyjmowany, a dozwolony zakres to 18–99 |
| Data, autor | 2026-11-25, [Twoje imię] |
| Środowisko | SklepTO 1.0 (XAMPP 8.2.12, PHP 8.2, MariaDB 10.4), Windows 10, Chrome [wersja] |
| Warunki wstępne | baza po `install.php?reset=1` |
| Kroki do odtworzenia | 1. Otwórz `http://localhost/sklepto/install.php?reset=1` (status OK). 2. Otwórz `http://localhost/sklepto/rejestracja.php`. 3. Wpisz dane testowe (poniżej) i zaznacz regulamin. 4. Kliknij „Zarejestruj". |
| Dane testowe | login: `reczny100`, e-mail: `nowy@example.com`, wiek: `100`, hasło: `Haslo123`, powtórz hasło: `Haslo123`, regulamin zaznaczony |
| Wynik oczekiwany | Specyfikacja: „wiek – liczba całkowita 18–99". Formularz powinien odrzucić wiek 100 komunikatem „Wiek musi być liczbą całkowitą z zakresu 18–99." |
| Wynik rzeczywisty | Konto zostało utworzone: „Konto zostało utworzone. Możesz się zalogować." Wiek 99 jest przyjmowany poprawnie, a 120 i 150 są odrzucane, więc błąd dotyczy dokładnie wartości 100 (górna granica zakresu) |
| Ważność / priorytet | średnia / niski |
| Test automatyczny | `test_rejestracja_awb.py::test_wiek_2p[100]`, `test_rejestracja_awb.py::test_wiek_3p[100]`, `test_rejestracja_dane.py::test_wiek_z_csv[AWB-100]` |
| Załączniki | zrzut ekranu strony z komunikatem „Konto zostało utworzone" po wpisaniu wieku 100, fragment raportu pytest (`raport.html`) |
| Status | Nowy |

---

# Raport defektu

| Pole | Wartość |
|---|---|
| Identyfikator | DEF-REJ-02 |
| Tytuł | Rejestracja (rejestracja.php): login z wielką literą (`Kowalski`) jest przyjmowany, a dozwolone są tylko małe litery, cyfry i `_` |
| Data, autor | 2026-11-25, [Twoje imię] |
| Środowisko | SklepTO 1.0 (XAMPP 8.2.12, PHP 8.2, MariaDB 10.4), Windows 10, Chrome [wersja] |
| Warunki wstępne | baza po `install.php?reset=1` |
| Kroki do odtworzenia | 1. Otwórz `http://localhost/sklepto/install.php?reset=1` (status OK). 2. Otwórz `http://localhost/sklepto/rejestracja.php`. 3. Wpisz dane testowe (poniżej) i zaznacz regulamin. 4. Kliknij „Zarejestruj". |
| Dane testowe | login: `Kowalski`, e-mail: `nowy@example.com`, wiek: `30`, hasło: `Haslo123`, powtórz hasło: `Haslo123`, regulamin zaznaczony |
| Wynik oczekiwany | Specyfikacja: „login 3–20 znaków `[a-z0-9_]`". Formularz powinien odrzucić login z wielką literą komunikatem „Login musi mieć od 3 do 20 znaków (małe litery, cyfry, _)." |
| Wynik rzeczywisty | Konto zostało utworzone: „Konto zostało utworzone. Możesz się zalogować." Ten sam efekt dla loginu `NowyUzytkownik`. Inne niedozwolone znaki (myślnik, kropka, spacja, polskie litery) są odrzucane poprawnie |
| Ważność / priorytet | średnia / średni |
| Test automatyczny | `test_rejestracja_ep.py::test_login_niepoprawny[wielkie-litery]`, `test_rejestracja_dane.py::test_login_z_csv[EP-wielkie-litery]` |
| Załączniki | zrzut ekranu strony z komunikatem „Konto zostało utworzone" po wpisaniu loginu `Kowalski`, fragment raportu pytest (`raport.html`) |
| Status | Nowy |