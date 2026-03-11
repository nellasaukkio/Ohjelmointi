# Luo yksi aktiviteetti kortti


def luo_uusikortti(nimi, kesto, edeltajat):
    return {
        'nimi': nimi,
        'kesto': kesto,
        'edeltajat': edeltajat,
        'seuraajat': []
        }


# Lisätään kortti kokoelmaan
def lisaa_kortti(kokoelma, kortti):
    kokoelma[kortti['nimi']] = kortti
def nayta_kortit(kortit):
    #tulostaa kortit
    print('Aktiviteetit')
    for nimi, kortti in kortit.items():
        print(f"  {kortti['nimi']}: {kortti['kesto']} tuntia")
    #tulostaa polut ja kestot
    print('Polut ja kestot')
    for nimi, kortti in kortit.items():
        print(f"  {kortti['nimi']}: {kortti['kesto']} tuntia, edeltäjät: {kortti['edeltajat']}, seuraajat: {kortti['seuraajat']}")
def nayta_polut(polut):
    for avain, polku in polut.items():
        print(f"Polkuryhmä {avain}:")
        print(f"  Nimet: {polku['nimet']}")
        print(f"  Avaimet: {polku['avaimet']}")
        print(f"  Kesto: {polku['tot_kesto']} tuntia")   


# Kysyy käyttäjältä kaikki kortit
def luo_kortti():
    kokoelma = {}
    print("Syötä aktiviteetit, tyhjä nimi lopettaa.")

    while True:
        nimi = input("Aktiviteetin nimi: ")
        if nimi == "":
            break

        kesto = int(input("Kesto (tuntia): "))
        edeltajat = input("Edeltäjät pilkulla erotettuna (tai tyhjä): ")

        if edeltajat.strip() == "":
            edeltajat = []
        else:
            edeltajat = [e.strip() for e in edeltajat.split(",")]

        kortti = luo_uusikortti(nimi, kesto, edeltajat)
        lisaa_kortti(kokoelma, kortti)
        print(f"Lisätty: {kortti}")
        print(f"Kokoelma nyt: {kokoelma}")

    return kokoelma



# Lisää seuraajat kokoelmaan
def hae_seuraajat(kokoelma):
    for nimi, kortti in kokoelma.items():
        for ed in kortti['edeltajat']:
            if ed in kokoelma:
                kokoelma[ed]['seuraajat'].append(nimi)



# Hakee aktiviteetit joilla ei ole edeltäjiä tai seuraajia
def hae_alku_lopetus_avaimet(kokoelma):
    alku = [n for n, k in kokoelma.items() if len(k['edeltajat']) == 0]
    loppu = [n for n, k in kokoelma.items() if len(k['seuraajat']) == 0]
    return alku, loppu

# Haetaan polut DFS:llä

def hae_polut(kokoelma, alku, loppu):
    kaikki_polut = []
    polku = []

    def dfs(nykyinen, polku):
        polku.append(nykyinen)

        if nykyinen in loppu:
            kaikki_polut.append(list(polku))

        for s in kokoelma[nykyinen]['seuraajat']:
            dfs(s, polku)

        polku.pop()

    for a in alku:
        dfs(a, polku)

    return kaikki_polut


# Luo polut ja laskee polkujen kestot
def rakenna_riippuvuudet(kokoelma):
    hae_seuraajat(kokoelma)
    alku, loppu = hae_alku_lopetus_avaimet(kokoelma)
    print(f"Alkuavaimet: {alku}, loppuavaimet: {loppu}")

    polut = hae_polut(kokoelma, alku, loppu)
    print(f'polut: {polut}')
    kaikki_polut = {}
    i = 0


    for p in polut:
        nimet = p
        avaimet = list(range(len(p)))
        tot_kesto = sum(kokoelma[n]['kesto'] for n in p)

        kaikki_polut[i] = {
            'avaimet': avaimet,
            'nimet': nimet,
            'tot_kesto': tot_kesto
        }
        i += 1

    return kaikki_polut

def main():
    print("=== Aktiviteettien riippuvuusanalyysi ===")

    # 1. Lue käyttäjän syöttämät kortit
    kortit = luo_kortti()

    print(kortit)

    # 2. Laske riippuvuudet ja polut
    kaikki_polut = rakenna_riippuvuudet(kortit)
    print(kaikki_polut)
    nayta_polut(kaikki_polut)
    # 3. Tulosta polut
    print("\n=== Kaikki polut ja niiden kestot ===")
    for avain, polut in kaikki_polut.items():
        print(f"Polkuryhmä {avain}:")
        print(polut)
        #for p, kesto, k in polut:
         
         #    print(f"  Polku: {p}, kesto: {kesto} kortti: {k}")

if __name__ == "__main__":
    main()