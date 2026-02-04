#  Tuo kirjastot ja anna niille lyhyemmät nimet
import matplotlib.pyplot as plt
import numpy as np

k=input('kulmakerroin: ')
#print(k, type(k))
k=float(k)
#print(k, type(k))

b=input('vakiotermi:')
b=float(b)
print(b,type(b))

x= np.linspace(-10,10,30)
#suoran yhtälö
y=k*x+b

# Luodaan kuva ja akselit
fig, ax = plt.subplots()

#  Suoran piirtäminen
plt.plot(x, y, color='red')

r=input('säde: ')
#print(r, type(r))
r=float(r)
#print(r, type(r))

o=input('keskipiste x arvo: ')
#print(o, type(o))
o=float(o)
#print(o,type(o))

i=input('keskipiste y arvo: ')
#print(i, type(i))
i=float(i)
#print(i, type(i))

# Luodaan kuva ja akselit


#  Luodaan ympyrä: (x, y) keskipiste, säde, väri
circle = plt.Circle((o, i),r, color='blue', fill=False)

#  Lisätään ympyrä akseleille
ax.add_patch(circle)

#  Asetetaan akselit samansuhteisiksi
ax.set_aspect('equal')

#luodaan kuva ja akselit
#  Suoran piirtäminen
plt.plot(x, y, color='red')
#näytetään kuva
plt.show()

#määritellään diskriminantin kirjaimet

V = 1 + k**2
W = -2*o + 2*k*(b - i)
U = o**2 + (b - i)**2 - r**2

# Diskriminantti
D = W**2 - 4*V*U
print("Diskriminantti D =", D)

# Leikkauspisteiden laskenta

if D < 0:
    print("Ei leikkauspisteitä")

elif D == 0:
    print("yksi leikkauspiste")

else:
    print("kaksi leikkauspistettä")

#leikkauspisteiden koordinaatit
if D>=0:
    x1=(-W+np.sqrt(D))/2*V
    y1=k*x1+b
    if D==0:
        print("leikkauspiste: ", x1, y1)
    else:
        x2=(-W-np.sqrt(D))/2*V
        y2=k*x2+b
        print("leikkauspiste 1: ", x1,y1)
        print("leikkauspiste 2: ", x2, y2)
