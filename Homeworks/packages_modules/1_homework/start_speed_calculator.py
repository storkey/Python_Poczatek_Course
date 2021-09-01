"""
Zadanie nr 1

Napisz funkcję obliczającą średnią prędkość biegu na podstawie czasu
i pokonanego dystansu (prędkość = dystans / czas) i umieść ją w jednym pliku.

W drugim pliku zaimportuj moduł, wczytaj informacje od użytkownika i wywołaj funkcję
- oblicz prędkość średnią.
"""
import speed_calculator

distance = float(input("Ile przebiegłeś km? "))
time = float(input("W ciągu ilu godzin? "))

avg_speed = speed_calculator.calculate_avg_speed(distance, time)

print(f"Przebiegając {distance:.2f} w czasie {time:.2f}, Twoja prędkość wyniosła {avg_speed:.2f} km/h.")
