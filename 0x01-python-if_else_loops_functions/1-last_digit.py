#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {0} is {1} ".format(number, number[-1])
        if number[-1] > 5:
        print("and is greater than 5")
        elif number[-1] == 0:
        print("and is zero")
        elif number[-1] < 6 != 0:
        print("and is less than 6 and not 0")
