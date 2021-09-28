class Product:

    def __init__(self, product_name, category_name, price_per_item):
        self.product_name = product_name
        self.category_name = category_name
        self.price_per_item = price_per_item


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


class Apple:

    def __init__(self, genre_name, size, price_per_kg):
        self.genre_name = genre_name
        self.size = size
        self.price_per_kg = price_per_kg


class Potato:

    def __init__(self, genre_name, size, price_per_kg):
        self.genre_name = genre_name
        self.size = size
        self.price_per_kg = price_per_kg
