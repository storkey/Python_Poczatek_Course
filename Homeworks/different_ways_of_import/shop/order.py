from shop.products import products


def create_order(ordered_product, ordered_quantity):
    order = {"product_name": ordered_product, "quantity": ordered_quantity}
    price = products[ordered_product]["price"]
    available_quantity = products[ordered_quantity]["quantity"]

    if available_quantity < ordered_quantity:
        print("Nie mamy tyle towaru")
        return None
