#1
def getSpotreba(druh_pohonne_hmoty):

    if druh_pohonne_hmoty == "nafta":
        return "35 l/100 km"
    elif druh_pohonne_hmoty == "benzín":
        return "30 l/100 km"
    elif druh_pohonne_hmoty == "elektro":
        return "180 kWh/100 km"
    elif druh_pohonne_hmoty == "hybrid":
        return "25 l/100 km"
    else:
        return "Neznámý druh pohonné hmoty"

print(getSpotreba("nafta"))
print(getSpotreba("elektro"))
print(getSpotreba("plyn"))

#2
def getNaklady(kilometry, druh_pohonne_hmoty="nafta"):

    ceny = {
        "nafta": 38.7,
        "benzín": 38.2,
        "elektro": 7.7,
        "hybrid": 38.4
    }


    spotreba = {
        "nafta": 35,
        "benzín": 30,
        "elektro": 180,
        "hybrid": 25
    }


    if druh_pohonne_hmoty not in ceny:
        return "Neznámý druh pohonné hmoty"


    spotreba_na_km = spotreba[druh_pohonne_hmoty] / 100
    cena_za_jednotku = ceny[druh_pohonne_hmoty]


    if druh_pohonne_hmoty == "elektro":
        naklady = (kilometry * spotreba_na_km) * cena_za_jednotku
    else:
        naklady = (kilometry * spotreba_na_km) * cena_za_jednotku

    return f"Náklady na {kilometry} km pro {druh_pohonne_hmoty}: {naklady:.2f} Kč"

print(getNaklady(480))
print(getNaklady(480, "benzín"))
print(getNaklady(480, "elektro"))
print(getNaklady(480, "hybrid"))

#3
from datetime import datetime, timedelta

def getSplatnost(datum=None):

    if datum is None:
        datum = datetime.today()
    else:

        datum = datetime.strptime(datum, "%Y-%m-%d")



    splatnost = datum + timedelta(days=30)


    return splatnost.strftime("%Y-%m-%d")
print(getSplatnost("2024-12-12"))
print(getSplatnost())

#4
def getSplatnost(datum=None):

    if datum is None:
        datum = datetime.today()
    else:

        datum = datetime.strptime(datum, "%Y-%m-%d")


    splatnost = datum + timedelta(days=30)


    return splatnost.strftime("%d. %m. %Y")


print(getSplatnost("2024-12-15"))


