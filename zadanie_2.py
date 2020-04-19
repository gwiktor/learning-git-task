import string

print("\n Zadanie 1 \n")
lista_zakupow = {
    "piekarnia" : ["chleb", "bułki", "masło"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

print("Lista zakupów")

for sklep, produkty in lista_zakupow.items():
    print("Idę do", sklep.capitalize(), "i kupuję tam:", produkty.capitalize())
count = 0 
    if isinstance(lista_zakupow[produkty], list): 
        count += len(lista_zakupow[produkty]) 
print("W sumie kupuję", count, "produktów")
