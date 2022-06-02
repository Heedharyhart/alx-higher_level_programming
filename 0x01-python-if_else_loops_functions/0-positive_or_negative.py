#!usr/bin/python
import random
number = random.randint(-10, 10)

if number > 0:
    print(f"{}is positive")
elif number == 0:
    print(f"{number} is Zero".format(number))
else:
    print(f"{number} is negative".format(number))
