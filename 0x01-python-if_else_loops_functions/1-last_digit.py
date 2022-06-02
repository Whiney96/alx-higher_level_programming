#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    x == - 1 * (-number % 10)
else:
    x == number % 10
print("Last digit of {0} is {1} ".format(number, x))
if x > 5:
    print("and is greater than 5")
elif x == 0:
    print("and is zero")
elif x < 6 != 0:
    print("and is less than 6 and not 0")
