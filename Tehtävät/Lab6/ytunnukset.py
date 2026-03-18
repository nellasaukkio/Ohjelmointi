
import requests
import json

#tarkista ja hae yritys
def tarkista(ytunnus: str):
    """
    Tarkistaa onko annettu y-tunnus validi.
    Palauttaa (True/False, seliteteksti)
    """

    # Muoto NNNNNNN-T
    if len(ytunnus) != 9 or ytunnus[7] != "-":
        return False, "Virheellinen muoto (oikea muoto NNNNNNN-T)"

    yksilointiosa = ytunnus[:7]
    tarkistusmerkki = ytunnus[-1]

    if not yksilointiosa.isdigit() or not tarkistusmerkki.isdigit():
        return False, "Tunnuksessa saa olla vain numeroita ja yksi väliviiva"

    painot = [7, 9, 10, 5, 8, 4, 2]

    summa = sum(int(yksilointiosa[i]) * painot[i] for i in range(7))
    jaannos = summa % 11

    if jaannos == 0:
        oikea = 0
    elif jaannos == 1:
        return False, "Tunnus ei voi olla käytössä (jakojäännös 1)"
    else:
        oikea = 11 - jaannos

    if oikea == int(tarkistusmerkki):
        return True, "Y-tunnus on validi"
    else:
        return False, "Virheellinen tarkistusmerkki"

def hae_yritys(ytunnus):
    """
    Hakee yrityksen tiedot PRH:n avoimesta datasta.
    Palauttaa dict: { 'y-tunnus', 'nimi', 'rekisteröity', 'osoite' }
    """

    headers = {
        'accept': 'application/json',
    }

    params = {
        'businessId': ytunnus,
    }

    response = requests.get(
        'https://avoindata.prh.fi/opendata-ytj-api/v3/companies',
        params=params, headers=headers)

    data = response.json()

    companies = data.get("companies", [])
    if not companies:
        return {}

    item = companies[0]

    yritys = {}

    # Y-tunnus
    yritys["y-tunnus"] = item.get("businessId", "")

    # Nimi ja rekisteröintipäivä
    if "names" in item and item["names"]:
        yritys["nimi"] = item["names"][0].get("name", "")
        yritys["rekisteröity"] = item["names"][0].get("registrationDate", "")

    # Osoite
    if "addresses" in item and item["addresses"]:
        a = item["addresses"][0]
        yritys["osoite"] = (
            f"{a.get('street', '')} {a.get('buildingNumber', '')}, "
            f"{a.get('postCode', '')} {a.get('postOffice', '')}"
        )

    return yritys
