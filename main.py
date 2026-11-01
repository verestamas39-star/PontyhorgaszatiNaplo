import tkinter as tk
import json
import statistics
from datetime import date
from tkinter import messagebox
from vt_modul import FogasVT, suly_ellenorzes_VT


root = tk.Tk()
root.title("Pontyhorgászati Napló")
root.geometry("800x700")

cim = tk.Label(root, text="Pontyhorgászati Napló", font=("Arial", 22))
cim.pack(pady=20)

adatlap = tk.Frame(root)
adatlap.pack(pady=10)

tk.Label(adatlap, text="Dátum:").grid(row=0, column=0, padx=10, pady=8)
datum_mezo = tk.Entry(adatlap, width=25)
datum_mezo.grid(row=0, column=1, padx=10, pady=8)
datum_mezo.insert(0, date.today().strftime("%Y-%m-%d"))

tk.Label(adatlap, text="Helyszín:").grid(row=1, column=0, padx=10, pady=8)
helyszin_mezo = tk.Entry(adatlap, width=25)
helyszin_mezo.grid(row=1, column=1, padx=10, pady=8)

tk.Label(adatlap, text="Halfaj:").grid(row=2, column=0, padx=10, pady=8)
halfaj_mezo = tk.Entry(adatlap, width=25)
halfaj_mezo.grid(row=2, column=1, padx=10, pady=8)
halfaj_mezo.insert(0, "Ponty")

tk.Label(adatlap, text="Súly (kg):").grid(row=3, column=0, padx=10, pady=8)
suly_mezo = tk.Entry(adatlap, width=25)
suly_mezo.grid(row=3, column=1, padx=10, pady=8)

fogasi_lista = tk.Listbox(root, width=80, height=12)
fogasi_lista.pack(pady=20)

fogasok = []



def fogasok_mentese_VT():
    adatok = []

    for fogas in fogasok:
        adatok.append({
            "datum": fogas.datum,
            "helyszin": fogas.helyszin,
            "halfaj": fogas.halfaj,
            "suly": fogas.suly
        })

    with open("fogasok.json", "w", encoding="utf-8") as fajl:
        json.dump(adatok, fajl, ensure_ascii=False, indent=4)



def fogasok_betoltese_VT():
    try:
        with open("fogasok.json", "r", encoding="utf-8") as fajl:
            adatok = json.load(fajl)

        for adat in adatok:
            fogas = FogasVT(
                adat["datum"],
                adat["helyszin"],
                adat["halfaj"],
                adat["suly"]
            )
            fogasok.append(fogas)
            fogasi_lista.insert(tk.END, fogas.megjelenit())

    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        messagebox.showerror("Hiba", "A mentett fájl nem olvasható!")


def statisztika_megjelenit_VT():
    if not fogasok:
        messagebox.showinfo("Statisztika", "Még nincs rögzített fogás!")
        return

    sulyok = [fogas.suly for fogas in fogasok]

    atlag = statistics.mean(sulyok)
    kozepso = statistics.median(sulyok)
    leggyakoribb = statistics.mode(sulyok)
    osszes = sum(sulyok)

    uzenet = (
        f"Fogások száma: {len(fogasok)} db\n"
        f"Összes kifogott hal: {osszes:.2f} kg\n"
        f"Átlagos súly: {atlag:.2f} kg\n"
        f"Középső súlyérték: {kozepso:.2f} kg\n"
        f"Leggyakoribb súly: {leggyakoribb:.2f} kg"
    )

    messagebox.showinfo("Horgászati statisztika", uzenet)


def fogas_torlese_VT():
    kijelolt = fogasi_lista.curselection()

    if not kijelolt:
        messagebox.showinfo("Törlés", "Először jelölj ki egy fogást!")
        return

    valasz = messagebox.askyesno(
        "Fogás törlése",
        "Biztosan törölni szeretnéd a kijelölt fogást?"
    )

    if valasz:
        index = kijelolt[0]
        fogasi_lista.delete(index)
        del fogasok[index]
        fogasok_mentese_VT()


def fogast_rogzit_VT():
    datum = datum_mezo.get()
    helyszin = helyszin_mezo.get()
    halfaj = halfaj_mezo.get()
    suly = suly_mezo.get()

    if not datum or not helyszin or not halfaj or not suly:
        messagebox.showwarning("Hiányzó adat", "Minden mezőt tölts ki!")
        return

    try:
        suly_kg = float(suly.replace(",", "."))
        if not suly_ellenorzes_VT(suly_kg):
            raise ValueError
    except ValueError:
        messagebox.showerror("Hibás adat", "A súly pozitív szám legyen!")
        return

    fogas = FogasVT(datum, helyszin, halfaj, suly_kg)
    fogasok.append(fogas)
    fogasi_lista.insert(tk.END, fogas.megjelenit())
    fogasok_mentese_VT()

    helyszin_mezo.delete(0, tk.END)
    suly_mezo.delete(0, tk.END)


rogzites_gomb = tk.Button(
    root,
    text="Fogás rögzítése",
    command=fogast_rogzit_VT,
    font=("Arial", 12)
)
rogzites_gomb.pack(pady=10)
statisztika_gomb = tk.Button(
    root,
    text="Statisztika",
    command=statisztika_megjelenit_VT,
    font=("Arial", 12)
)
statisztika_gomb.pack(pady=5)

torles_gomb = tk.Button(
    root,
    text="Kijelölt fogás törlése",
    command=fogas_torlese_VT,
    font=("Arial", 12)
)
torles_gomb.pack(pady=5)

fogasok_betoltese_VT()
root.mainloop()