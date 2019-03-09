# calc_functions.py
# Create a program that can calculate using +, -, /, and *.

def main():
    equation = input("Enter the equation")
    equationlist = str.split(equation)
    i = 0
    while len(equationlist) > 1:
        if len(equationlist) > i:
            if equationlist[i] == "*":
                x = int(equationlist[i-1])
                y = int(equationlist[i+1])
                print(x,y)
                equationlist.insert(i, (x * y))
                print(equationlist)
                del equationlist[i+1]
                print(equationlist)
                del equationlist[i+1]
                print(equationlist)
                del equationlist[i-1]
                print(equationlist)
                print(i)
            elif equationlist[i] == "/":
                x = int(equationlist[i-1])
                y = int(equationlist[i+1])
                print(x,y)
                equationlist.insert(i, (x / y))
                print(equationlist)
                del equationlist[i+1]
                print(equationlist)
                del equationlist[i+1]
                print(equationlist)
                del equationlist[i-1]
                print(equationlist)
                print(i)
            elif i < len(equationlist):
                i = i + 1
        elif len(equationlist) == i and i > 1:
            i = 0
            while len(equationlist) > 1:
                if len(equationlist) > i:
                    if equationlist[i] == "+":
                        x = int(equationlist[i-1])
                        y = int(equationlist[i+1])
                        print(x,y)
                        equationlist.insert(i, (x + y))
                        print(equationlist)
                        del equationlist[i+1]
                        print(equationlist)
                        del equationlist[i+1]
                        print(equationlist)
                        del equationlist[i-1]
                        print(equationlist)
                        print(i)
                    elif equationlist[i] == "-":
                        x = int(equationlist[i-1])
                        y = int(equationlist[i+1])
                        print(x,y)
                        equationlist.insert(i, (x - y))
                        print(equationlist)
                        del equationlist[i+1]
                        print(equationlist)
                        del equationlist[i+1]
                        print(equationlist)
                        del equationlist[i-1]
                        print(equationlist)
                        print(i)
                    elif i < len(equationlist):
                        print(i)
                        i = i + 1
        else:
            break
    print("The answer is", int(equationlist[0]))

main()
