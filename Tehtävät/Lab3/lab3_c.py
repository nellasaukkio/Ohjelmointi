#ohjelmaan käytetty copilot tekoälyä
#Tekoälylle syötetty lab3_b.py tehtävän tehtävänanto ja pyydetty kirjoittamaan ohjelma, joka toteuttaa tehtävänannon
#lisäksi pyydetty piirtämään yksi pylväsdiagrammi, jossa on 100 pylvästä ja kaikki kolme mittaria ovat samassa kuvassa

import random
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------
# Kassajonon simulointi (yhden 6h = 360min kierroksen)
# -----------------------------------------
def simulate_queue(p_arrival, p_service):
    queue = 0
    max_queue = 0
    idle_time = 0
    customers_served = 0

    for minute in range(360):  # 6 h simulaatio
        # 1. Uusi asiakas saapuu
        if random.random() < p_arrival:
            queue += 1
            if queue > max_queue:
                max_queue = queue

        # 2. Palvelu
        if queue > 0:
            if random.random() < p_service:
                queue -= 1
                customers_served += 1
        else:
            idle_time += 1

    return customers_served, max_queue, idle_time


# -----------------------------------------
# Pääohjelma
# -----------------------------------------
def main():
    pA = float(input("Anna todennäköisyys A (asiakkaan saapuminen): "))
    pB = float(input("Anna todennäköisyys B (palvelun valmistuminen): "))

    results_customers = []
    results_max_queue = []
    results_idle = []

    # 100 simulaatiota
    for i in range(100):
        c, mq, idle = simulate_queue(pA, pB)
        results_customers.append(c)
        results_max_queue.append(mq)
        results_idle.append(idle)

    # -----------------------------------------
    # 3 mittaria samaan kuvaan eri väreillä
    # -----------------------------------------

    x = np.arange(1, 101)          # x-akseli 1–100
    width = 0.25                    # pylvään leveys

    plt.figure(figsize=(16, 6))

    plt.bar(x - width, results_customers, width=width,
            color="green", label="Asiakkaat")
    plt.bar(x, results_max_queue, width=width,
            color="blue", label="Max jonon pituus")
    plt.bar(x + width, results_idle, width=width,
            color="red", label="Tyhjäaika")

    plt.title("Simulaation tulokset (100 simulaatiokierrosta)")
    plt.xlabel("Simulaatiokierros")
    plt.ylabel("Arvo")
    plt.legend()
    plt.tight_layout()
    plt.show()


# -----------------------------------------
# Suoritus
# -----------------------------------------
if __name__ == "__main__":
    main()