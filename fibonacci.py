# fibonacci.py
# Create a program that displays specified numbers in the fibonacci sequence.

def main ():
    x = 1
    y = 1
    n = eval(input("Please enter a number"))
    if n < 3:
        print ("1")
    else:
        for i in range (0, n-2):
            z = x + y
            x = y
            y = z
        print (z)

main ()
