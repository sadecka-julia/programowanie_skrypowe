import math
import sys


def prime_numbers(number):
    if number == 2:
        return True
    if number <= 1:
        return False
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i <= number**(1/2):
        if number % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    arr = sys.argv[1:]
    for number in arr:
        try:
            if prime_numbers(int(number)):
                print(number)
        except ValueError:
            print("error")


