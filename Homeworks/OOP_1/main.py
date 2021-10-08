from shop.apple import Apple
from shop.order import Order, create_order_with_products, print_order
from shop.potato import Potato
from shop.product import Product

if __name__ == "__main__":

    green_apple = Apple(genre_name="Ligol", size="L", price_per_kg=8.50)
    red_apple = Apple(genre_name="Ligol", size="S", price_per_kg=7.00)
    young_potato = Potato(genre_name="Bryza", size="M", price_per_kg=6.00)
    normal_potato = Potato(genre_name="Bryza", size="L", price_per_kg=5.00)

    products = []
    first_product = Product(product_name="Ciastka", category_name="Słodycze", price_per_item=2.5)
    products.append(first_product)
    second_product = Product(product_name="Kalafior", category_name="Warzywa", price_per_item=4)
    products.append(second_product)
    third_product = Product(product_name="Chleb", category_name="Pieczywo", price_per_item=3.5)
    products.append(third_product)

    first_order = Order(first_name="Jan", last_name="Kowalski", products=products)
    second_order = create_order_with_products("Norman", "Normalny")

    second_product.print_product()
    print_order(first_order)
    print("\n\n")
    print_order(second_order)
