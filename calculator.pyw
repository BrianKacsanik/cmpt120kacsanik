#calc_window.py
#Create a graphic window that functions as a calculator.

from graphics import *

class Button:
    def __init__(self, name, coords, labels, color, size):
        self.name = name
        self.coords = coords
        self.labels = labels
        self.color = color
        self.size = size
        
def buttonsize(i, x, y):
    buttonsize = Rectangle(Point(x,y),Point(x+buttons[i].size,y+buttons[i].size))
    return buttonsize

buttons = [Button("memadd", [35,88], 'M+', 'orange', 40),
           Button("memsub", [85,88], 'M-', 'orange', 40),
           Button("memrecall", [135,88], 'MR', 'orange', 40),
           Button("memclear", [185,88], 'MC', 'orange', 40),
           Button("button7", [35,134], '7', 'lightblue', 40),
           Button("button8", [85,134], '8', 'lightblue', 40),
           Button("button9", [135,134], '9', 'lightblue', 40),
           Button("buttondiv", [185,134], '/', 'orange', 40),
           Button("button4", [35,180], '4', 'lightblue', 40),
           Button("button5", [85,180], '5', 'lightblue', 40),
           Button("button6", [135,180], '6', 'lightblue', 40),
           Button("buttonmult", [185,180], '*', 'orange', 40),
           Button("button1", [35,226], '1', 'lightblue', 40),
           Button("button2", [85,226], '2', 'lightblue', 40),
           Button("button3", [135,226], '3', 'lightblue', 40),
           Button("buttonadd", [185,226], '+', 'orange', 40),
           Button("buttonneg", [35,272], '+/-', 'orange', 40),
           Button("button0", [85,272], '0', 'lightblue', 40),
           Button("buttondecimal", [135,272], '.', 'lightblue', 40),
           Button("buttonsub", [185,272], '-', 'orange', 40),
           Button("buttondel", [135,318], 'Del', 'orange', 40),
           Button("buttonequal", [185,318], '=', 'orange', 40)]

def createcanvas():
    win = GraphWin("Calculator", 260, 371)
    win.setBackground("navy")
    return win

def createdisplay(win):
    display = Rectangle(Point(35,75),Point(225,29))
    display.setFill("teal")
    display.draw(win)

def inside(point, rectangle):

    rectp1 = rectangle.getP1()
    rectp2 = rectangle.getP2()

    return rectp1.getX() < point.getX() < rectp2.getX() and rectp1.getY() < point.getY() < rectp2.getY()

def createbuttons(win):
    for i in range(len(buttons)):
        x = buttons[i].coords[0]
        y = buttons[i].coords[1]
        button = Rectangle(Point(x,y),Point(x+buttons[i].size,y+buttons[i].size))
        button.setFill(buttons[i].color)
        label = Text(Point(x+buttons[i].size/2,y+buttons[i].size/2),buttons[i].labels)
        button.draw(win)
        label.draw(win)

def calculate(win):
    equationlist = []
    memlist = []
    buttonpress = 0
    displaytext = Text(Point(130,52),"")
    displaytext.draw(win)
    numberkey = [4,5,6,8,9,10,12,13,14,17,18]
    pressedbutton = 0
    while True:
        if pressedbutton == "=":
            break
        buttonpress = win.getMouse()
        for i in range(len(buttons)):
            if buttonpress is None:
                displaytext.setText("")
            else:
                if len(equationlist) < 1:
                    displaytext.setText("")
                else:
                    screen = ""
                    for q in equationlist:
                        screen = screen + q
                    displaytext.setText(screen)
            x = buttons[i].coords[0]
            y = buttons[i].coords[1]
            if inside(buttonpress, buttonsize(i, x, y)):
                pressedbutton = buttons[i].labels
                if buttonpress == "=":
                    break
                elif i in numberkey:
                    equationlist.extend(buttons[i].labels)
                elif pressedbutton == "+":
                    equationlist.extend(" + ")
                elif pressedbutton == "-":
                    equationlist.extend(" - ")
                elif pressedbutton == "*":
                    equationlist.extend(" * ")
                elif pressedbutton == "/":
                    equationlist.extend(" / ")
                elif pressedbutton == "+/-":
                    equationlist.extend("-")
                elif pressedbutton == "Del":
                    if len(equationlist) > 0:
                        if equationlist[-1] == " ":
                            del equationlist[-1]
                            del equationlist[-1]
                            del equationlist[-1]
                        else:
                            del equationlist[-1]
                elif pressedbutton == "M+":
                    g = ""
                    for f in equationlist:
                        g = g + f
                    equation = str.split(g)
                    memlist.extend(equation[-1])
                    if memlist[-1] == "+" or memlist[-1] == "-" or memlist[-1] == "*" or memlist[-1] == "/":
                        del memlist[-1]
                elif pressedbutton == "M-":
                    if len(memlist) > 0:
                        del memlist[-1]
                elif pressedbutton == "MR":
                    if len(memlist) > 0:
                        g = ""
                        for f in memlist:
                            g = g + f
                        equation = str.split(g)
                        equationlist.extend(equation[-1])
                elif pressedbutton == "MC":
                    memlist = []
                elif pressedbutton == "=":
                    g = ""
                    for f in equationlist:
                        g = g + f
                    equation = str.split(g)
                    break
    
    i = 0
    while len(equation) > 1:
        if len(equation) > i:
            if equation[i] == "*":
                x = float(equation[i-1])
                y = float(equation[i+1])
                equation.insert(i, (x * y))
                del equation[i+1]
                del equation[i+1]
                del equation[i-1]
            elif equation[i] == "/":
                x = float(equation[i-1])
                y = float(equation[i+1])
                if y == 0:
                    equation = "ERROR"
                    break
                else:
                    equation.insert(i, (x / y))
                    del equation[i+1]
                    del equation[i+1]
                    del equation[i-1]
            elif i < len(equation):
                i = i + 1
        elif len(equation) == i and i > 1:
            i = 0
            while len(equation) > 1:
                if len(equation) > i:
                    if equation[i] == "+":
                        x = float(equation[i-1])
                        y = float(equation[i+1])
                        equation.insert(i, (x + y))
                        del equation[i+1]
                        del equation[i+1]
                        del equation[i-1]
                    elif equation[i] == "-":
                        x = float(equation[i-1])
                        y = float(equation[i+1])
                        equation.insert(i, (x - y))
                        del equation[i+1]
                        del equation[i+1]
                        del equation[i-1]
                    elif i < len(equation):
                        i = i + 1
        else:
            break
    if equation == "ERROR":
        displaytext.setText(equation)
    else:
        displaytext.setText(equation[0])

def main():
    win = createcanvas()
    createdisplay(win)
    createbuttons(win)
    calculate(win)

main()
