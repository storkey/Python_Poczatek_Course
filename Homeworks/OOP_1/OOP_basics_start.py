"""
    Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.

    Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.

    Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy produktów,
    a wartościami instancje klasy produkt.

    Konstruktor i pola obiektu (zadania)

    Zadanie nr 1

    Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order, Apple i Potato:

    Product: nazwa, nazwa kategorii, cena jednostkowa
    Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta), łączna cena
    (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
    Apple: nazwa gatunku, rozmiar, cena za kg
    Potato: nazwa gatunku, rozmiar, cena za kg

    Utwórz kilka obiektów każdej klasy.


    Zadanie nr 2

    Napisz funkcję wypisującą produkt i zamówienie. Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.

    Zadanie nr 3

    Napisz funkcję generującą zamówienie z losową listą produktów na przykład: Produkt-1, Produkt-2 itd.
"""
from OOP_basics.classes import Apple, Potato, Order, Product


def print_product(product):
    print(f"Nazwa: {product.product_name}, Kategoria: {product.category_name},"
          f" Cena: {product.price_per_item} zł za sztukę.")


if __name__ == "__main__":

    green_apple = Apple(genre_name="Ligol", size="L", price_per_kg=8.50)
    red_apple = Apple(genre_name="Ligol", size="S", price_per_kg=7.00)
    young_potato = Potato(genre_name="Bryza", size="M", price_per_kg=6.00)
    normal_potato = Potato(genre_name="Bryza", size="L", price_per_kg=5.00)

    products = []
    first_product = Product(product_name="Ciastka", category_name="Słodycze", price_per_item=2.5)
    products.append(first_product)
    second_product = Product(product_name="Kalafior", category_name="Warzywa", price_per_item=4)
    products.append(second_product)
    third_product = Product(product_name="Chleb", category_name="Pieczywo", price_per_item=3.5)
    products.append(third_product)

    first_Order = Order(first_name="Jan", last_name="Kowalski", products=products)

    print("Type of green_apple is:", type(green_apple))
    print("Type of red_apple is:", type(red_apple))
    print("Type of young_potato is:", type(young_potato))
    print("Type of normal_potato is:", type(normal_potato))
