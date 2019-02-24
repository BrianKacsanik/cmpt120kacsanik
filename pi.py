# pi.py
# Create a program that approximates the value of pi.

import math

def main():
    n =eval(input("Enter a number"))
    approx = 0
    for i in range(n):
        approx = approx + 4 * (-1) ** i / (2 * i + 1)
    print(approx)
    print(math.pi - approx)

main()
