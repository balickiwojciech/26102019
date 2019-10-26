import csv

def prepare_data(wartosc):
    #print(balance)
    wartosc = wartosc.replace("$", "")
    #print(balance)
    wartosc = wartosc.replace(",", "")
    #print(balance)
    kwota = float(wartosc)
    if isinstance(kwota, float):
        #print(type)
        return kwota

def analisis(lista):

    srednia = sum(lista)/len(lista)
    return srednia

def wyciagnij_srednia(csv_file):
    lista = []
    for row in csv_file:
        #print(row["balance"])
        wartosc = row["balance"]

        #prepare_data(row["balance"])
        kwota = prepare_data(wartosc)
        lista.append(kwota)
    #     print(lista)
    # analisis(lista)
    wynik = analisis(lista)
    return wynik
    #return round(wynik, 2)

def wypisz_wiersze(csv_file):
    for row in csv_file:
        print(row["balance"])

with open("../resources/data.csv") as plik:
    csv_file = csv.DictReader(plik)

    print(wyciagnij_srednia(csv_file))



