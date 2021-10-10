class Apple:

    def __init__(self, genre_name, size, kg):
        self.genre_name = genre_name
        self.size = size
        self.kg = kg
        self.price_per_kg = 3.5

    def total_price(self):
        total_price = self.kg * self.price_per_kg
        return f"{round(total_price, 2)}"
