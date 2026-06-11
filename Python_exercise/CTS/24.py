from math import *

def math_operations(number):
    if number < 0:
        return "Invalid input"

    print("Square Root:", sqrt(number))
    print("Power:", pow(number, 2))
    print("PI Value:", pi)

math_operations(4)