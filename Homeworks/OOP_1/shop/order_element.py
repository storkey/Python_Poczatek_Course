from shop.product import Product


class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
