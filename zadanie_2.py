import string

print("\n Zadanie 1 \n")
lista_zakupow = {
    "piekarnia" : ["chleb", "bułki", "masło"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

print("Lista zakupów")

suma = 0
for sklep, produkty in lista_zakupow.items():
    produkty = [produkt.capitalize() for produkt in produkty]
    print("Idę do", sklep.capitalize(), "i kupuję tam:", produkty)
    #Prostsze policzenie sumy produktów
    count = len(produkty)
    suma = suma + count
print("W sumie kupuję", suma, "produktów")
