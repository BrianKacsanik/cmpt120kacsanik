# fibonacci.py
# Create a program that displays specified numbers in the fibonacci sequence.

def main ():
    x = 1
    y = 1
    n = eval(input("Please enter a number"))
    if n is 1:
        print ("1")
    if n > 1:
        for i in range (1, n):
            z = x + y
            x = y
            y = z
        print (z)

main ()
