import random
import time

import matplotlib
import matplotlib.pyplot as plt

A=input('Millä todennäköisyydellä asiakas tulee kassalle (0-1): ')
#print(A, type(A))
A=float(A)
#print(A, type(A))

B=input('Millä todennäköisyydellä palvelu tulee valmiiksi (0,1): ')
#print(B, type(B))
B=float(B)
#print(B, type(B))

for round in range(100):

    #  luo kassa, jossa asioi ja jonottaa satunnainen määrä asiakkaita
    kassajono = 0
    asiakas = 0
    ticks = 360  # Simuloi 6 tuntia, 3600 sekuntia / 10 = 360 "minuuttia"
    #  tilastoja kassa toiminnasta
    tyhjaaika = 0
    max_kassajono = 0
    palvellut_asiakkaat = 0 
    max_tyhjaaika = 0



    while ticks > 0:
        if random.random() < A:  # Satunnaisesti päätetään, saapuuko uusi asiakas
            asiakas += 1
            kassajono += 1
            if kassajono > max_kassajono:
                max_kassajono = kassajono  # Päivitä maksimi kassajono
            
        #time.sleep(0.1)  # Simuloi minuutin kulumista
        if kassajono > 0:
            tyhjaaika = 0  # Kassa ei ole tyhjä, nollaa tyhjäaika
            if random.random() < B:  # Satunnaisesti päätetään onko asiakkaan 
                #  palvelu valmis vai onko asiakkaallla vielä ostoksia
                kassajono -= 1  # poista palveltu asiakas jonosta
                palvellut_asiakkaat += 1
        elif kassajono == 0:
            tyhjaaika += 1  # Kassa on tyhjä, lisää tyhjäaikaa
            if tyhjaaika > max_tyhjaaika:
                max_tyhjaaika = tyhjaaika  # Päivitä maksimi tyhjäaika  
        #print(ticks, kassajono*"*")

        ticks -= 1 # Vähennä yksi "minuutti" simulaatiosta
    '''
    print(f"Simulaation lopussa oli {kassajono} asiakasta jonossa.")
    print(f"Simulaation aikana palvellut asiakkaat: {palvellut_asiakkaat}")
    print(f"Simulaation aikana suurin kassajono: {max_kassajono} asiakasta")
    print(f"Simulaation aikana suurin tyhjäaika: {max_tyhjaaika} minuuttia")
    '''
    plt.bar(round, palvellut_asiakkaat, color='blue')
    plt.bar(round+0.1, max_kassajono, color='red')
    plt.bar(round+0.2, max_tyhjaaika, color='green')

plt.show()