"""
Zadanie nr 1

Napisz prosty symulator sklepu.

W jednym pliku zdefiniuj dostępne produkty: nazwę (np. chleb i jabłka), dostępną ilość i cenę jednostkową.
W innym zaimplementuj funkcję, która na podstawie nazwy produktu i zamawianej ilości stworzy nowe zamówienie i
doda je do listy zamówień. Zamówienie składa się z nazwy produktu, zamówionej ilości i łącznej ceny.
Obydwa pliki umieść w pakiecie.

Sklep uruchom poprzez plik main, w którym zaimportujesz funkcje do tworzenia zamówienia, wczytasz dane od użytkownika
 i wypiszesz łączny koszt zakupów. Zastosuj importowanie absolutne postaci from … import.

Zadanie nr 2

Zmodyfikuj poprzednie rozwiązanie zamieniając import wewnątrz pakietu z absolutnego na względny.


Zadanie nr 3

Zmodyfikuj rozwiązanie zadania pierwszego zamykając logikę w pliku main w funkcję, która wywoła się tylko
jeżeli skrypt ten zostanie bezpośrednio uruchomiony __name__ → __main__.
"""
from shop.order import create_order
from shop.products import products

print("Witaj w naszym sklepie!")
print("Oto nasze produkty:")
counter = 1
for product, quantity in products.items():
    print(f"\t{counter}. {product} sztuk: {quantity['quantity']}")
    counter += 1

product_name = input("\nPodaj nazwę produktu, który chcesz kupić: ")
product_quantity = input("Ile sztuk? ")

create_order(product_name, product_quantity)
