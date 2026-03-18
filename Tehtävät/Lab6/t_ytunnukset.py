#tuodaan kirjastot
import tkinter as tk
from tkinter import filedialog as fd
from pathlib import Path
import json
import ytunnukset

yritys = {}

options = {
    'defaultextension': '.json',
    'filetypes': [('json files', '.json'), ('text files', '.txt'), ('all files', '.*')],
    'initialdir': Path.home() / "Desktop",
    'initialfile': ''
}

def tarkista_ja_hae(tunnus):
    global yritys

    validi, teksti = ytunnukset.tarkista(tunnus)

    if not validi:
        yritys = {}
        return teksti

    yritys = ytunnukset.hae_yritys(tunnus)

    if not yritys:
        return "Yritystä ei löytynyt"

    return json.dumps(yritys, indent=2, ensure_ascii=False)
#lue window
def lue(window):
    global yritys
    options['parent'] = window

    filename = fd.askopenfilename(title='Open file', **options)
    if not filename:
        return "Ei tiedostoa valittu"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                yritys = data
                return json.dumps(yritys, indent=2, ensure_ascii=False)
            else:
                return "Tiedosto ei sisältänyt dict-tyyppistä dataa"
    except Exception as e:
        return f"Virhe tiedostoa luettaessa: {e}"

def tallenna(window):
    options['parent'] = window

    filename = fd.asksaveasfilename(title='Save the file', **options)
    if not filename:
        return

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(yritys, f, indent=2, ensure_ascii=False)

def main():
    ikkuna = tk.Tk()
    ikkuna.geometry('300x250')
    ikkuna.title('Y-tunnus')

    tk.Label(ikkuna, text="Y-tunnus").grid(row=0, column=0, pady=5)
    entry = tk.Entry(ikkuna, width=12)
    entry.grid(row=0, column=1, pady=5)

    label = tk.Label(ikkuna, text='', anchor="w", justify="left")
    label.grid(row=2, column=0, columnspan=3, rowspan=3, sticky=tk.EW, padx=5, pady=5)

    ikkuna.rowconfigure(2, weight=1)
    ikkuna.columnconfigure(0, weight=1)

    tk.Button(
        ikkuna,
        text='Tarkista',
        command=lambda: label.config(text=tarkista_ja_hae(entry.get()))
    ).grid(row=1, column=1, pady=5)

    tk.Button(
        ikkuna,
        text='Tallenna',
        command=lambda: tallenna(ikkuna)
    ).grid(row=6, column=0, pady=10)

    tk.Button(
        ikkuna,
        text='Näytä tallennetut',
        command=lambda: [label.config(text=lue(ikkuna)), entry.delete(0, 'end')]
    ).grid(row=6, column=1, pady=10)

    ikkuna.mainloop()

if __name__ == "__main__":
    main()
