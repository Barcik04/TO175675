# Ćwiczenia 5 – pliki startowe

Skopiuj zawartość tego katalogu do projektu z ćwiczeń 4 i uruchom `pytest -v`.
Na starcie: **3 passed, 20 skipped**, 1 xfailed oraz `test_drag_and_drop_actionchains` jako xpassed albo xfailed.
Testy do napisania mają `pytest.skip("TODO")` – usuń tę linię i uzupełnij test zgodnie z instrukcją.

| Plik | Kroki | Co jest gotowe |
|---|---|---|
| `config.py` | – | adresy stron (`INTERNET_URL`) |
| `conftest.py` | 7 | fixture `driver`, hook ze zrzutem ekranu przy porażce |
| `pytest.ini` | 1 | marker `slow` |
| `test_waits.py` | 1–2 | antywzorzec `sleep`, oba testy implicit wait |
| `test_dynamic_controls.py` | 3 | lokalizatory |
| `test_alerts.py` | 4 | `click_button`, `result_text`, `test_alert` |
| `test_frames_windows.py` | 5–6 | `body_text`, `h3_text` |
| `test_actions.py` | 8–12 | `JS_DRAG_AND_DROP`, `loaded_paragraphs`, `test_drag_and_drop_actionchains` |

Kod (nazwy, komentarze) jest po angielsku. Bez okna przeglądarki (PowerShell): `$env:HEADLESS="1"; pytest -q`
