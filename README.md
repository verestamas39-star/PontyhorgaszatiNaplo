# Pontyhorgászati Napló

**Készítette:** Veres Tamás

## A program célja

A program egy egyszerű, grafikus felületű pontyhorgászati napló. Segítségével rögzíthetjük a horgászat során kifogott halak adatait, például a dátumot, a helyszínt, a halfajt és a hal súlyát.

A program az adatokat JSON-fájlban tárolja, így azok a program újraindítása után is megmaradnak.

## Felhasznált modulok

- `tkinter`: grafikus felület létrehozása és eseménykezelés.
- `json`: adatok mentése és visszatöltése.
- `datetime`: aktuális dátum kezelése.
- `statistics`: statisztikai számítások.

## Saját modul

**vt_modul.py**

A saját modul tartalmazza:

- `suly_ellenorzes_VT()`: ellenőrzi, hogy a megadott súly pozitív szám-e.
- `FogasVT`: saját osztály, amely a fogás adatait tárolja.
- `megjelenit()`: a fogás adatainak szöveges megjelenítése.

## Főbb függvények

A `main.py` fájlban található függvények:

- `fogasok_mentese_VT()`: a fogások mentése JSON-fájlba.
- `fogasok_betoltese_VT()`: a korábban mentett fogások betöltése.
- `fogast_rogzit_VT()`: új fogás rögzítése.
- `statisztika_megjelenit_VT()`: statisztikai adatok kiszámítása és megjelenítése.
- `fogas_torlese_VT()`: kijelölt fogás törlése.

## Statisztikai számítások

A program a `statistics` modul három függvényét használja:

- `mean()`: átlagos súly kiszámítása.
- `median()`: medián kiszámítása.
- `mode()`: leggyakoribb súlyérték meghatározása.

## Adattárolás

A fogások adatai a `fogasok.json` fájlban kerülnek tárolásra.

## A program használata

1. A dátum megadása.
2. A horgászat helyszínének megadása.
3. A halfaj megadása.
4. A hal súlyának megadása.
5. A fogás rögzítése.
6. A rögzített fogások megtekintése.
7. Statisztika megjelenítése.
8. Kijelölt fogás törlése.