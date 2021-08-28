"""
Zadanie nr 3

Napisz kalkulator obliczający wartość lokaty po pewnym czasie.

Wczytaj od użytkownika informacje o:

    Początkowym kapitale (wpłaconej kwocie)
    Oprocentowaniu
    Okresie trwania inwestycji (w latach)

Umieść funkcję obliczająca wartość lokaty w pakiecie calculations,
a wczytanie danych i uruchomienie obliczeń w pliku powyżej pakietu.

Skorzystaj ze wzoru: wartość = wartość pocz. * (1 + procent/100) ^ liczba lat
"""
import calculations.investment_calculator


def ask_for_float(message):
    input_value = input(message)
    return int(input_value)


initial_capital = ask_for_float("Podaj wartość kapitału początkowego: ")
percentage = ask_for_float("Podaj oprocentowanie lokaty: ")
years = ask_for_float("Podaj na ile lat jest lokata: ")

investment_value = calculations.investment_calculator.calculate_investment(initial_capital, percentage, years)

print(f"Twoja lokata, przy kapitale początkowym: {initial_capital:.2f} zł, oprocentowaniu: {percentage:.2f}%"
      f", zawarta na: {years:.2f} lat, da końcowo: {investment_value:.2f} zł")
