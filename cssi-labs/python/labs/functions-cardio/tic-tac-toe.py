winner = ""
gameBoard = [
    ["x", "o", " "],
    ["o", "o", "x"],
    ["x", "o", " "]
]

def checkWin(board) {
    for row in board: #checking for row wins
        if (row[0] == row[1] and row[2] == row[0]):
            print "There has been a winner!"
            return True
    for i in range(3): #checking for column wins
        if board[0][i] == board[1][i] and board[2][i] == board[0][i]:
            print "There has been a winner!"
            return True
    
}

print gameBoard
