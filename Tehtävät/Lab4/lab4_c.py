#tässä tehtävässä käytetetty copilot tekoälyä
#Tekoäylle annettu tehtäväanto: Tee Python-ohjelma, joka hakee aineistosta parempaa korrelaatiota tyytyväisyyden ja jonkun muun sarakkeen kesken kuin oma valintasi. Aineiston nimi on data1.xlsx ja kansiorakennne "C:\Users\nella\Documents\Tuotantotalous\1. Vuosi\Ohjelmointi\data1.xlsx" oma korrelaationi oli 0.325164
#lisäksi annoin tehtävänannossa kuvan itsin tehtävänannosta lab4_b.py tehtävään

import pandas as pd
import matplotlib.pyplot as plt

# 1. Lue Excel
df = pd.read_excel(
    r"C:\Users\nella\Documents\Tuotantotalous\1. Vuosi\Ohjelmointi\data1.xlsx",
    engine="openpyxl"
)

# 2. Laske kokonaistyytyväisyys (5 osatekijää)
osa_sarakkeet = ['johto', 'työtov', 'työymp', 'palkkat', 'työteht']
df['tyytyväisyys'] = df[osa_sarakkeet].mean(axis=1)

# 3. Sarakkeet, joita verrataan tyytyväisyyteen
selite_sarakkeet = ['palkka', 'perhe', 'sukup', 'ikä', 'koulutus', 'palveluv']

# 4. Laske korrelaatiot näistä sarakkeista
korrelaatiot = df[selite_sarakkeet + ['tyytyväisyys']].corr(numeric_only=True)['tyytyväisyys']
korrelaatiot = korrelaatiot.drop('tyytyväisyys')

print("\nKorrelaatiot kokonaistyytyväisyyteen verrattuna:\n")
print(korrelaatiot.sort_values(ascending=False))

# 5. Etsi paras korrelaatio
paras = korrelaatiot.abs().idxmax()
print(f"\nParas selittävä sarake on: {paras} (korrelaatio {korrelaatiot[paras]:.3f})")

# 6. Scatter-kuva parhaasta sarakkeesta
plt.scatter(df[paras], df['tyytyväisyys'])
plt.xlabel(paras)
plt.ylabel("tyytyväisyys")
plt.title(f"Korrelaatio: {paras} vs tyytyväisyys ({korrelaatiot[paras]:.3f})")
plt.show()