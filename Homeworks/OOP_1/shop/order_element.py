from shop.product import Product


class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_total_price(self):
        return self.product.price_per_item * self.quantity

    def print_order_element(self):
        self.product.print_product()
        print(f"\tLiczba sztuk {self.quantity}, cena sumarycznie: {self.calculate_total_price()} zł")
