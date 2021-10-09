from shop.product import Product


class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def print_order_element(self):
        self.product.print_product()
        print(f"\tLiczba sztuk {self.quantity}")
