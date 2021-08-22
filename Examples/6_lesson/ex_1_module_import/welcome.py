import math

import hello

hello.say_hello()
name = input("Jak masz na imię? ")
hello.say_hello_with_name(name)

print("pi:", math.pi)

sinus_180 = math.sin(math.pi)
print("sinus_180", sinus_180)

print("math.inf", math.inf)

very_big_number = 100_000_000_000_000
the_biggest_number = math.inf

print('the_biggest_number > very_big_number:', the_biggest_number > very_big_number)
