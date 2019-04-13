# CMPT 120 Intro to Programming
# Lab #7 – Lists and Error Handling
# Author: Brian Kacsanik
# Created: 2019-04-12
symbol = [ " ", "x", "o" ]

def printRow(row):
    # initialize output to the left border
    output = "|"
    # for each square in the row...
    for i in range(3):
        # add to output the symbol for this square followed by a border
        output = output + " " + symbol[row[i]] + " |"
    # print the completed output for this row
    print(output)
	
def printBoard(board):
    # print the top border
    print("+-----------+")
    # for each row in the board...
    for i in range(3):
        # print the row
        printRow(board[i])
        # print the next border
        print("+-----------+")
	
def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    if board[row][col] == 0:
        # if so, set it to the player number
        board[row][col] = player
        return True
    else:
        print("Non empty location. Pick another one")
        return False
	
def getPlayerMove():
    row = int(input("Enter a row for the play (1-3):")) 
    col = int(input("Enter a column for the play (1-3):"))
    return (row - 1, col - 1) 
	
def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    checkboard = []
    for i in board:
        checkboard.extend(i)
    if 0 in checkboard:
        return True
    else:
        return False

def victory(board,player):
    player = player % 2 + 1
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] > 0:
        printBoard(board)
        print("Congratulations Player", player)
        return False
    elif board[0][0] == board[0][1] == board[0][2] and board[0][0] > 0:
        printBoard(board)
        print("Congratulations Player", player)
        return False
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] > 0:
        printBoard(board)
        print("Congratulations Player", player)
        return False
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] > 0:
        printBoard(board)
        print("Congratulations Player", player)
        return False
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] > 0:
        printBoard(board)
        print("Congratulations Player", player)
        return False
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] > 0:
        printBoard(board)
        print("Congratulations Player", player)
        return False
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] > 0:
        printBoard(board)
        print("Congratulations Player", player)
        return False
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] > 0:
        printBoard(board)
        print("Congratulations Player", player)
        return False
    else:
        return True
	
def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    player = 1
    while hasBlanks(board):
        if victory(board,player) is True:
            printBoard(board)
            row,col = getPlayerMove()
            if markBoard(board,row,col,player) is True:
                player = player % 2 + 1 # switch player for next turn
        else:
            break

main()
