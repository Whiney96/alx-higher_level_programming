#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number[-1]
print("Last digit of {0} is {1} ".format(number, num))
if num > 5:
    print("and is greater than 5")
elif num == 0:
    print("and is zero")
elif num < 6 != 0:
    print("and is less than 6 and not 0")
