"""
Zadanie nr 2

Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta na podstawie otrzymanych
długości przyprostokątnych.

Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.

Wykorzystaj w tym celu moduł math z biblioteki standardowej oraz funkcje:

    sqrt(x) - liczy pierwiastek drugiego stopnia z podanej wartości x
    pow(x, y) - podnosi x do potęgi y

"""

import math


def calculate_hypotenuse(a_len, b_len):
    return math.sqrt(math.pow(a_len, 2) + math.pow(b_len, 2))


a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))

c = calculate_hypotenuse(a, b)
print(f"Przy długości boków: a = {a:.2f} i b = {b:.2f}, c = {c:.2f}")
