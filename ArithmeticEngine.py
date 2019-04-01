# CMPT 120 - Lab #6
# Brian Kacsanik
# 1-4-2019
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = str.lower(input("What computation do you want to perform? "))
        if cmd == "add":
            function(cmd)
            break
        elif cmd == "sub":
            function(cmd)
            break
        elif cmd == "mult":
            function(cmd)
            break
        elif cmd == "div":
            function(cmd)
            break
        elif cmd == "quit":
            break
        else:
            print(cmd, "is not a valid command")
            break

def function(cmd):
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if cmd == "add":
            result = num1 + num2
            print("The result is " + str(result) + ".\n")
        elif cmd == "sub":
            result = num1 - num2
            print("The result is " + str(result) + ".\n")
        elif cmd == "mult":
            result = num1 * num2
            print("The result is " + str(result) + ".\n")
        elif cmd == "div":
            try:
                result = num1 / num2
                print("The result is " + str(result) + ".\n")
            except:
                if num2 == 0:
                    print("Unable to devide by zero.")
                    result = 0
    except:
        print("That is not a valid number")
        function(cmd)


def main():
    showIntro()
    doLoop()
    showOutro()

main()
