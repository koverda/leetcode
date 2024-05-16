import os


class TicTacToe:
    board = []
    gameOver = False
    moves = 0

    def __init__(self):
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(" ")

    def drawBoard(self):
        for i in range(3):
            for j in range(3):
                print(f'[{self.board[i][j]}]', end="")
            print("")
        print("")

    # starts from top left
    # column coords are letters
    # row coords are numbers
    # a1 = top left
    def markSquare(self, letter, number, marker):
        row = int(number) - 1
        column = int(ord(letter[0].lower()) - ord('a'))
        self.board[row][column] = marker
        self.drawBoard()

    def checkWin(self):
        # check horiz
        for i in range(len(self.board[0])):
            row = self.board[i]
            rowSet = set(row)
            if len(rowSet) == 1 and rowSet.pop() != " ":
                return True

        # check vert
        for i in range(len(self.board[0])):
            colSet = set()
            for j in range(len(self.board)):
                colSet.add(self.board[j][i])
            if len(colSet) == 1 and colSet.pop() != " ":
                return True

        return False

        # check diag


ttt = TicTacToe()
ttt.drawBoard()
ttt.markSquare('b', 1, 'x')
ttt.markSquare('b', 2, 'x')
ttt.markSquare('b', 3, 'x')
res = ttt.checkWin()
print(res)
