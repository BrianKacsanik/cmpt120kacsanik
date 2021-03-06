#calc_window.py
#Create a graphic window that functions as a calculator.

from graphics import *

def createcanvas():
    win = GraphWin("Calculator", 260, 325)
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
    coords = [[35,88],[85,88],[135,88],[185,88],
              [35,134],[85,134],[135,134],[185,134],
              [35,180],[85,180],[135,180],[185,180],
              [35,226],[85,226],[135,226],[185,226],
              [135,272],[185,272]]
    labels = ['7','8','9','/',
              '4','5','6','x',
              '1','2','3','+',
              '+/-','0','.','-',
              "Del","="]
    color = ['lightblue','lightblue','lightblue','orange',
             'lightblue','lightblue','lightblue','orange',
             'lightblue','lightblue','lightblue','orange',
             'orange','lightblue','lightblue','orange',
             'orange','orange']
    size = [40,40,40,40,
            40,40,40,40,
            40,40,40,40,
            40,40,40,40,
            40,40]
    for i in range(len(coords)):
        x = coords[i][0]
        y = coords[i][1]
        button = Rectangle(Point(x,y),Point(x+size[i],y+size[i]))
        button.setFill(color[i])
        label = Text(Point(x+size[i]/2,y+size[i]/2),labels[i])
        button.draw(win)
        label.draw(win)

def calculate(win):
    equationlist = []
    buttonpress = 0
    button1 = Rectangle(Point(35,180),Point(75,220))
    button2 = Rectangle(Point(85,180),Point(125,220))
    button3 = Rectangle(Point(135,180),Point(175,220))
    button4 = Rectangle(Point(35,134),Point(75,174))
    button5 = Rectangle(Point(85,134),Point(125,174))
    button6 = Rectangle(Point(135,134),Point(175,174))
    button7 = Rectangle(Point(35,88),Point(75,128))
    button8 = Rectangle(Point(85,88),Point(125,128))
    button9 = Rectangle(Point(135,88),Point(175,128))
    button0 = Rectangle(Point(85,226),Point(125,266))
    buttonadd = Rectangle(Point(185,180),Point(225,220))
    buttonsub = Rectangle(Point(185,226),Point(225,266))
    buttonmult = Rectangle(Point(185,134),Point(225,174))
    buttondiv = Rectangle(Point(185,88),Point(225,128))
    buttonneg = Rectangle(Point(35,226),Point(75,266))
    buttondel = Rectangle(Point(135,272),Point(175,312))
    buttondecimal = Rectangle(Point(135,226),Point(175,266))
    buttonequal = Rectangle(Point(185,272),Point(225,312))
    displaytext = Text(Point(145,52),"")
    displaytext.draw(win)
    while True:
        if buttonpress == "=":
            # You should include your call to resolve the equation here.
            break
        else:
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
            buttonpress = win.getMouse()
            if inside(buttonpress, button1):
                equationlist.extend("1")
            elif inside(buttonpress, button2):
                equationlist.extend("2")
            elif inside(buttonpress, button3):
                equationlist.extend("3")
            elif inside(buttonpress, button4):
                equationlist.extend("4")
            elif inside(buttonpress, button5):
                equationlist.extend("5")
            elif inside(buttonpress, button6):
                equationlist.extend("6")
            elif inside(buttonpress, button7):
                equationlist.extend("7")
            elif inside(buttonpress, button8):
                equationlist.extend("8")
            elif inside(buttonpress, button9):
                equationlist.extend("9")
            elif inside(buttonpress, button0):
                equationlist.extend("0")
            elif inside(buttonpress, buttonadd):
                equationlist.extend(" + ")
            elif inside(buttonpress, buttonsub):
                equationlist.extend(" - ")
            elif inside(buttonpress, buttonmult):
                equationlist.extend(" * ")
            elif inside(buttonpress, buttondiv):
                equationlist.extend(" / ")
            elif inside(buttonpress, buttondecimal):
                equationlist.extend(".")
            elif inside(buttonpress, buttonneg):
                equationlist.extend("-")
            elif inside(buttonpress, buttondel):
                del equationlist[-1]
            elif inside(buttonpress, buttonequal):
                g = ""
                for f in equationlist:
                    g = g + f
                equation = str.split(g)
                break
    i = 0
    while len(equation) > 1:
        if len(equation) > i:
            if equation[i] == "*":
                x = int(equation[i-1])
                y = int(equation[i+1])
                equation.insert(i, (x * y))
                del equation[i+1]
                del equation[i+1]
                del equation[i-1]
            elif equation[i] == "/":
                x = int(equation[i-1])
                y = int(equation[i+1])
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
                        x = int(equation[i-1])
                        y = int(equation[i+1])
                        equation.insert(i, (x + y))
                        del equation[i+1]
                        del equation[i+1]
                        del equation[i-1]
                    elif equation[i] == "-":
                        x = int(equation[i-1])
                        y = int(equation[i+1])
                        equation.insert(i, (x - y))
                        del equation[i+1]
                        del equation[i+1]
                        del equation[i-1]
                    elif i < len(equation):
                        i = i + 1
        else:
            break
    displaytext.setText(equation[0])

def main():
    win = createcanvas()
    createdisplay(win)
    createbuttons(win)
    calculate(win)

main()
