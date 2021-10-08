class Product:

    def __init__(self, product_name, category_name, price_per_item):
        self.product_name = product_name
        self.category_name = category_name
        self.price_per_item = price_per_item

    def print_product(self):
        print(f"\tNazwa: {self.product_name}, Kategoria: {self.category_name},"
              f" Cena: {self.price_per_item:.2f} zł za sztukę.")
