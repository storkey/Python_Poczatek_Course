"""
    Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.

    Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.

    Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy produktów,
    a wartościami instancje klasy produkt.
"""

from OOP_basics.classes import Apple, Potato, Order, Product

if __name__ == "__main__":
    green_apple = Apple()
    red_apple = Apple()
    young_potato = Potato()
    normal_potato = Potato()

    print("Type of green_apple is:", type(green_apple))
    print("Type of red_apple is:", type(red_apple))
    print("Type of young_potato is:", type(young_potato))
    print("Type of normal_potato is:", type(normal_potato))

    orders = []
    for order in range(5):
        orders.append(Order())
    print(orders)

    products = {
        "Bryza": Product(),
        "Ligol": Product(),
        "Szynka": Product(),
        "Ser": Product(),
        "Majonez": Product()
    }

    for key, value in products.items():
        print(f"\t{key}: {value}")
