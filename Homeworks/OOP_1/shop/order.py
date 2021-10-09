import random

from shop.order_element import OrderElement
from shop.product import Product


class Order:

    def __init__(self, first_name, last_name, ordered_elements=None):
        self.first_name = first_name
        self.last_name = last_name

        if ordered_elements is None:
            ordered_elements = []
        self.ordered_elements = ordered_elements

        total_price = 0
        for order_element in ordered_elements:
            total_price += order_element.calculate_total_price()
        self.total_price = total_price

    def print_order(self):
        print(30 * "*")
        print(f"Imię: {self.first_name}, Nazwisko: {self.last_name}")
        print(30 * "*")
        print("Zamówione produkty:")

        for ordered_element in self.ordered_elements:
            ordered_element.print_order_element()
            print(5 * "-")
        print(f"Cena łączna: {self.total_price:.2f} zł")


def create_order_with_products(first_name, last_name):
    ordered_elements = []
    for number in range(random.randint(1, 20)):
        product_name = f"Produkt-{number}"
        categories = ["Pieczywo", "Warzywa", "Słodycze"]
        number_of_category = random.randint(0, 2)
        category = categories[number_of_category]
        price_per_item = round(random.uniform(2, 5), 2)
        quantity = random.randint(1, 10)
        ordered_elements.append(OrderElement(Product(product_name, category, price_per_item), quantity))

    return Order(first_name, last_name, ordered_elements)
