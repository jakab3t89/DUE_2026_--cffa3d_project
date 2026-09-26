# Vonatút-napló

## Hallgató

### Jakab Tibor - CFFA3D - DUEL-ISR-116-HU_2026-2027-1

## Feladat leírása

Egyszerű vonatút-napló grafikus felülettel (Tkinter). Fel lehet írni, honnan hova és mikor utaztam vonattal, és ki lehet törölni egy utat. Az utak az `utak.txt` fájlba mentődnek, így újraindítás után is megmaradnak.

## Modulok és függvények

### Tanult modulok

- `tkinter` –- grafikus felület (ablak, feliratok, beviteli mezők, gombok, lista), `messagebox.showwarning()`
- `
os` –- `os.path.exists()`: megnézi, létezik-e már az `utak.txt`

### Bemutatandó modul: `datetime`

- `datetime.now()` –- a mai dátum és idő lekérése
- `
strftime()` –- dátumból szöveg (`2026-09-25` formában)
- `
datetime.strptime()` –- szövegből dátum, ezzel ellenőrzöm, hogy jó-e a beírt dátum

### Saját modul: `trip_JT.py`

- `JT_today()` –- a mai dátum szövegként
- `
JT_check_date(text)` –- jó-e a beírt dátum
- `
JT_load_trips()` –- utak betöltése a fájlból
- `
JT_save_trips(trips)` –- utak mentése a fájlba
- `
JT_add_trip(trip, trips)` –- új út hozzáadása és mentése
- `
JT_remove_trip(trip, trips)` –- út törlése és mentése

## Osztályok

### `class_JT.py`

- `Trip_JT` –- egy vonatút adatai (honnan, hova, dátum), `get_info()` metódus

### `ui_JT.py`

- `App_JT` –- a grafikus felület és az eseménykezelés (gombok, Enter billentyű)

## Program felépítése

- **Indítás:** `main.py`
- **
Alapablak:** `root`
- **
Programnév:** `app` (Vonatút-napló JT)
- **
Szükséges modulok:** csak a Python beépített moduljai (`tkinter`, `os`, `datetime`), külön telepíteni nem kell semmit.