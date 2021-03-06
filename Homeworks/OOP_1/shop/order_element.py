class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_element_total_price(self):
        return self.product.price_per_item * self.quantity

    def print_order_element(self):
        self.product.print_product()
        print(f"\tLiczba sztuk {self.quantity}, cena sumarycznie: {self.calculate_element_total_price() :.2f} zł")
