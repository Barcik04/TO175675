## B2
Drugi przebieg: `test_poprawna_rejestracja` pada z komunikatem „Login jest już zajęty.". Dane z pierwszego przebiegu zostały w bazie, więc testy zależą od stanu bazy i potrzebny jest reset.

## B3
`unikalny_login()` daje za każdym razem inny login, więc w jednej sesji testy nie kolidują. Reset raz na sesję usuwa dane z poprzedniego uruchomienia, bo licznik startuje od nowa.

## B4
1. `POPRAWNE` i `KOMUNIKATY` zgadzają się ze specyfikacją.
2. `type=number` blokuje litery. Zmiana na `text` pozwala przetestować walidację serwera.
3. Wstawia unikalny login, jeśli test nie podał własnego.
4. Jeden błąd pokazuje, że winne jest tylko badane pole.


# Rejestracja SklepTO – klasy równoważności i wartości brzegowe

Specyfikacja: login 3–20 znaków `[a-z0-9_]`, unikalny; e-mail poprawny; wiek – liczba całkowita 18–99;
hasło 8–20 znaków, co najmniej jedna litera i jedna cyfra; hasła identyczne; regulamin zaznaczony.

## 1. Klasy równoważności (EP)

| Pole | Klasy poprawne (reprezentant) | Klasy niepoprawne (reprezentant) |
|---|---|---|
| login | P1: 3–20 znaków `[a-z0-9_]`, unikalny (`unikalny_login()`) | N1: krótszy niż 3 (`ab`); N2: dłuższy niż 20 (21 × `a`); N3: wielkie litery / niedozwolony znak (`Jan!`); N4: zajęty (`jan`) |
| e-mail | P2: poprawny (`nowy@example.com`) | N5: brak `@` (`nowyexample.com`); N6: brak domeny (`nowy@`); N7: pusty |
| wiek | P3: liczba całkowita 18–99 (`30`) | N8: poniżej 18 (`10`); N9: powyżej 99 (`150`); N10: nie liczba (`abc`); N11: niecałkowita (`30.5`); N12: pusty |
| hasło | P4: 8–20 znaków, litera i cyfra (`Haslo123`) | N13: za krótkie (`Abc123`); N14: za długie (21 znaków); N15: bez cyfry (`Haslohaslo`); N16: bez litery (`12345678`); N17: puste |
| haslo2 | P5: identyczne z hasłem | N18: różne (`Inne1234`) |
| regulamin | P6: zaznaczony | N19: niezaznaczony |

Liczba przypadków testowych: 20 (1 poprawny + 19 niepoprawnych)  Pokrycie EP: 25 / 25 = 100 %

## 2. AWB – wiek (klasa poprawna 18–99)

| Wariant | Wartości | Oczekiwany wynik |
|---|---|---|
| 2-punktowa | 17, 18, 99, 100 | 17: błąd; 18: OK; 99: OK; 100: błąd |
| 3-punktowa | 17, 18, 19, 98, 99, 100 | 17: błąd; 18, 19, 98, 99: OK; 100: błąd |

## 3. AWB – długość loginu (3–20)

| Wariant | Długości | Oczekiwany wynik |
|---|---|---|
| 2-punktowa | 2, 3, 20, 21 | 2: błąd; 3: OK; 20: OK; 21: błąd |
| 3-punktowa | 2, 3, 4, 19, 20, 21 | 2: błąd; 3, 4, 19, 20: OK; 21: błąd |

## 4. AWB – długość hasła (8–20)

| Wariant | Długości | Oczekiwany wynik |
|---|---|---|
| 2-punktowa | 7, 8, 20, 21 | 7: błąd; 8: OK; 20: OK; 21: błąd |
| 3-punktowa | 7, 8, 9, 19, 20, 21 | 7: błąd; 8, 9, 19, 20: OK; 21: błąd |

## 5. Wyniki testów

| Test (id) | Wynik na Twoim SklepTO (PASS/FAIL) | Uwagi |
|---|---|---|
| test_poprawna_rejestracja | PASS | |
| test_login_niepoprawny[za-krotki] | PASS | |
| test_login_niepoprawny[za-dlugi] | PASS | |
| test_login_niepoprawny[wielkie-litery] | **FAIL** | login `Kowalski` przyjęty („Konto zostało utworzone"), a spec dopuszcza tylko małe litery – defekt |
| test_login_niepoprawny[myslnik] | PASS | |
| test_login_niepoprawny[spacja] | PASS | |
| test_login_niepoprawny[polskie-litery] | PASS | |
| test_login_niepoprawny[pusty] | PASS | |
| test_login_zajety | PASS | |
| test_unikalnosc_loginu | PASS | |
| test_email_niepoprawny[bez-malpy, bez-domeny, bez-nazwy, dwie-malpy, pusty] | PASS (5/5) | |
| test_wiek_niepoprawny[ponizej, powyzej, ulamek, tekst, pusty] | PASS (5/5) | |
| test_haslo_niepoprawne[za-krotkie, za-dlugie, bez-cyfry, bez-litery, puste] | PASS (5/5) | |
| test_hasla_rozne | PASS | |
| test_brak_regulaminu | PASS | |
| test_przegladarka_filtruje_litery_w_polu_wiek | PASS | walidacja klienta |
| test_wiek_2p[17, 18, 99] | PASS (3/3) | |
| test_wiek_2p[100] | **FAIL** | wiek 100 przyjęty („Konto zostało utworzone"), a spec: max 99 – defekt górnej granicy |
| test_wiek_3p[17, 18, 19, 98, 99] | PASS (5/5) | |
| test_wiek_3p[100] | **FAIL** | ten sam defekt co w 2p |
| test_login_dlugosc_2p[2, 3, 20, 21] | PASS (4/4) | |
| test_login_dlugosc_3p[2, 3, 4, 19, 20, 21] | PASS (6/6) | |
| test_haslo_dlugosc_2p[7, 8, 20, 21] | PASS (4/4) | |
| test_haslo_dlugosc_3p[7, 8, 9, 19, 20, 21] | PASS (6/6) | |
| test_wiek_z_csv[EP-poprawny, EP-ponizej, EP-powyzej, EP-ulamek, EP-tekst, EP-pusty, AWB-17, AWB-18, AWB-19, AWB-98, AWB-99] | PASS (11/11) | |
| test_wiek_z_csv[AWB-100] | **FAIL** | wiek 100 przyjęty – ten sam defekt co w AWB |
| test_login_z_csv[EP-poprawny, EP-kropka, EP-pusty, AWB-2, AWB-3, AWB-4, AWB-19, AWB-20, AWB-21] | PASS (9/9) | |
| test_login_z_csv[EP-wielkie-litery] | **FAIL** | login `NowyUzytkownik` przyjęty – ten sam defekt co `Kowalski` |

Razem: 80 testów (28 EP + 30 AWB + 22 CSV), 75 PASS, 5 FAIL.

Porównanie 2p vs 3p – czy wariant 3-punktowy wykrył coś więcej? Dlaczego?

Nie, w tym przypadku wariant 3-punktowy nie wykrył nic więcej. Defekt (przyjęcie wieku 100) wykryły oba warianty, 
bo wartość 100 leży tuż poza zakresem i jest w obu zestawach. Dodatkowe punkty 3p (19 i 98 dla wieku, 4 i 19 dla loginu, 9 i 19 dla hasła) 
przeszły. Wariant 3p mógłby wykryć więcej, gdyby błąd dotyczył wartości tuż wewnątrz zakresu, np. gdyby serwer odrzucał 19 albo 98.
Tutaj taki błąd nie występuje.



