#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
_number = abs(number) % 10
if number < 0:
    _number -= _number
print("Last digit of {} is {} and is ".format(number, _number), end="")
if number > 5:
    print("greater than 5")
elif number == 0:
    print("0")
else:
    print("less than 6 and not 0")
