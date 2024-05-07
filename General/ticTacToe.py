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

    def markSquare(self, letter, number, marker):
        i = int(number) - 1
        l = int(ord(letter[0].lower()) - ord('a'))
        self.board[i][l] = marker
        self.drawBoard()



ttt = TicTacToe()
ttt.drawBoard()
ttt.markSquare('a', 1, 'x')
ttt.markSquare('b', 3, 'o')