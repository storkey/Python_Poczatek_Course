from shop.products import products, update_product_quantity


def create_order(ordered_product, ordered_quantity):
    price = products[ordered_product]["price"]
    available_quantity = products[ordered_quantity]["quantity"]

    if available_quantity < ordered_quantity:
        print("Nie mamy tyle towaru")
        return None

    total_price = ordered_quantity * price
    order = {
        "product": ordered_product,
        "quantity": ordered_quantity,
        "total_price": total_price
    }
    update_product_quantity(ordered_product, ordered_quantity)
    return order
