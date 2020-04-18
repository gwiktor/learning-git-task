import string

print("\n Zadanie 1 \n")
lista_zakupow = {
    "piekarnia" : ["chleb", "bułki", "masło"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

print("Lista zakupów")

for sklep, produkty in lista_zakupow.items():
    print("Idę do", sklep.capitalize(), "i kupuję tam:", produkty)
count = 0
for produkt in lista_zakupow: 
    if isinstance(lista_zakupow[produkt], list): 
        count += len(lista_zakupow[produkt]) 
print("W sumie kupuję", count, "produktów")