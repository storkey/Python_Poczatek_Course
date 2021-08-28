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

initial_capital = float(input("Podaj wartość kapitału początkowego: "))
percentage = float(input("Podaj oprocentowanie lokaty: "))
years = float(input("Podaj na ile lat jest lokata: "))
