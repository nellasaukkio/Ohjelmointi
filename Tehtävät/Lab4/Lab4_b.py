#tuodaan kirjastot
import pandas as pd
import matplotlib.pyplot as plt
#Hae datatiedosto ja luetaan se dataframeen
df = pd.read_excel(r"C:\Users\nella\Documents\Tuotantotalous\1. Vuosi\Ohjelmointi\data1.xlsx")
#Haetaan df:tä uuteen dataframeen df2 sarakkeet, jotka kuvaavat tyytyväisyyttä eri kategoriossa
df2 = df[['palkkat', 'johto', 'työtov', 'työymp','työteht']]


#laske osatyytyväisyyksistä kokonaistyytyväisyys eli keskiarvo
df2['tyytyväisyys'] = df2.mean(axis=1)
print(df2)
#haetaan sukupuoli ja palkka
df2 = df2.join(df[['palkka','sukup']])
df2.corr()
print(df2.corr())

#piirretään kuvaaja, jossa x-akselilla on kokonaistyytyväisyys ja y-akselilla palkka
plt.scatter(df2['tyytyväisyys'], df2['palkka'])
plt.xlabel('kokonaistyytyväisyys')  
plt.ylabel('Palkka')
plt.title('Kokonaistyytyväisyys vs Palkka')
plt.show()

#piirretään kuvaaja, jossa x-akselilla on kokonaistyytyväisyys ja y-akselilla sukupuoli
plt.scatter(df2['tyytyväisyys'], df2['sukup'])
plt.xlabel('kokonaistyytyväisyys')  
plt.ylabel('Sukupuoli')
plt.title('Kokonaistyytyväisyys vs Sukupuoli')
plt.show()
