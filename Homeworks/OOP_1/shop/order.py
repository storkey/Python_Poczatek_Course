import random

from shop.product import print_product, Product


class Order:

    def __init__(self, first_name, last_name, products=None):
        self.first_name = first_name
        self.last_name = last_name

        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.price_per_item
        self.total_price = total_price

    def print_order(self):
        print(f"Imię: {self.first_name}, Nazwisko: {self.last_name}\nZamówione produkty:")
        for product in self.products:
            print_product(product)
        print(f"Cena łączna: {self.total_price:.2f} zł")


def create_order_with_products(first_name, last_name):
    ordered_products = []
    for number in range(random.randint(1, 20)):
        product_name = f"Produkt-{number}"
        categories = ["Pieczywo", "Warzywa", "Słodycze"]
        number_of_category = random.randint(0, 2)
        category = categories[number_of_category]
        price_per_item = round(random.uniform(2, 5), 2)
        ordered_products.append(Product(product_name, category, price_per_item))

    return Order(first_name, last_name, ordered_products)
