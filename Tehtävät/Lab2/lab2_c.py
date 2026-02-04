import numpy as np
import matplotlib.pyplot as plt

# --- KÄYTTÄJÄN SYÖTTEET ---
k = float(input("Anna suoran kulmakerroin k: "))
b = float(input("Anna suoran vakiotermi b: "))

x0 = float(input("Anna ympyrän keskipisteen x0: "))
y0 = float(input("Anna ympyrän keskipisteen y0: "))
r = float(input("Anna ympyrän säde r: "))

# --- TOISEN ASTEEN YHTÄLÖ: A x^2 + B x + C = 0 ---
# Suora: y = kx + b
# Ympyrä: (x - x0)^2 + (y - y0)^2 = r^2
# Sijoitus tuottaa:
# (x - x0)^2 + (kx + b - y0)^2 = r^2

A = 1 + k**2
B = -2*x0 + 2*k*(b - y0)
C = x0**2 + (b - y0)**2 - r**2

# --- DISKRIMINANTTI ---
D = B**2 - 4*A*C

print("\nLeikkauspisteet:")

if D > 0:
    # kaksi ratkaisua
    x1 = (-B + np.sqrt(D)) / (2*A)
    x2 = (-B - np.sqrt(D)) / (2*A)
    y1 = k*x1 + b
    y2 = k*x2 + b
    print(f"Kaksi leikkauspistettä:\n({x1}, {y1}) ja ({x2}, {y2})")

elif D == 0:
    # yksi ratkaisu
    x = -B / (2*A)
    y = k*x + b
    print(f"Yksi leikkauspiste (tangentti):\n({x}, {y})")

else:
    print("Ei leikkauspisteitä.")

# --- PIIRTÄMINEN ---
theta = np.linspace(0, 2*np.pi, 400)
circle_x = x0 + r*np.cos(theta)
circle_y = y0 + r*np.sin(theta)

line_x = np.linspace(x0 - r - 5, x0 + r + 5, 400)
line_y = k*line_x + b

plt.figure()
plt.plot(circle_x, circle_y, label="Ympyrä")
plt.plot(line_x, line_y, label="Suora")
plt.gca().set_aspect("equal", adjustable="box")
plt.legend()
plt.title("Suoran ja ympyrän leikkaus")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
