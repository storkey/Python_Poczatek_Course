class Product:

    def __init__(self, product_name, category_name, price_per_item):
        self.product_name = product_name
        self.category_name = category_name
        self.price_per_item = price_per_item


def print_product(product):
    print(f"\tNazwa: {product.product_name}, Kategoria: {product.category_name},"
          f" Cena: {product.price_per_item:.2f} zł za sztukę.")
