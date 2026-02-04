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
fig, ax = plt.subplots()

#  Luodaan ympyrä: (x, y) keskipiste, säde, väri
circle = plt.Circle((o, i),r, color='blue', fill=False)

#  Lisätään ympyrä akseleille
ax.add_patch(circle)

#  Asetetaan akselit samansuhteisiksi
ax.set_aspect('equal')



#määritellään diskriminantin kirjaimet

V = 1 + k**2
W = -2*o + 2*k*(b - i)
U = o**2 + (b - i)**2 - r**2

# --- Diskriminantti ---
D = W**2 - 4*V*U
print("\nDiskriminantti D =", D)

# --- Leikkauspisteiden laskenta ---
points = []

       


if D < 0:
    print("Ei leikkauspisteitä")

elif D == 0:
    # yksi piste
    x = -W / (2*V)
    y = k*x + b
    points.append((x, y))
    print("Yksi leikkauspiste:")
    print(f"Piste: ({x:.3f}, {y:.3f})")

else:
    # kaksi pistettä
    sqrtD = np.sqrt(D)
    x1 = (-W + sqrtD) / (2*V)
    x2 = (-W - sqrtD) / (2*V)
    y1 = k*x1 + b
    y2 = k*x2 + b

    points.append((x1, y1))
    points.append((x2, y2))

    print("Kaksi leikkauspistettä:")
    print(f"P1 = ({x1:.3f}, {y1:.3f})")
    print(f"P2 = ({x2:.3f}, {y2:.3f})")



# Ympyrä
circle = plt.Circle((o, i), r, color='blue', fill=False)
ax.add_patch(circle)

# Suora
x_vals = np.linspace(o - r - 5, o + r + 5, 400)
y_vals = k*x_vals + b
plt.plot(x_vals, y_vals, color='red')

# Piirretään leikkauspisteet jos olemassa
for px, py in points:
    plt.plot(px, py, 'go')  # vihreä piste
    plt.text(px, py, f"({px:.2f},{py:.2f})")

ax.set_aspect('equal')
plt.grid(True)
plt.show()