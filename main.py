class Tictactoe():
    board = []

    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        return [
            ['1', '|', '2', '|', '3'],
            ['-', '+', '-', '+', '-'],
            ['4', '|', '5', '|', '6'],
            ['-', '+', '-', '+', '-'],
            ['7', '|', '8', '|', '9'],
        ]

    def display_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end='')
            print('')

    def start(self):
        self.display_board()

if __name__ == '__main__':
    tictactoe = Tictactoe()
    tictactoe.start()