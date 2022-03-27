class Tictactoe:
    player, bot = '', ''
    redo = True

    def __init__(self, player, bot):
        self.player = player
        self.bot = bot

    def header(self):
        print('================================================')
        print('\tWelcome to Minimax Tictactoe!')
        print('================================================')

    def display_board(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                print(board[i][j], end='')
            print('')

    def check_moves(self, board):
        for i in range(0, len(board), 2):
            for j in range(0, len(board), 2):
                if type(board[i][j]) == int:
                    return True
        return False

    def evaluate_board(self, board):
        # checking for row
        for i in range(0, len(board), 2):
            if board[i][0] == board[i][2] and board[i][2] == board[i][4]:
                if board[i][0] == self.bot:
                    return 10
                elif board[i][0] == self.player:
                    return -10

        # checking for column
        for i in range(0, len(board), 2):
            if board[0][i] == board[2][i] and board[2][i] == board[4][i]:
                if board[0][i] == self.bot:
                    return 10
                elif board[0][i] == self.player:
                    return -10

        # left diagonal
        left = 0
        if board[left][left] == board[left + 2][left + 2] and board[left + 2][left + 2] == board[left + 4][left + 4]:
            if board[left][left] == self.bot:
                return 10
            elif board[left][left] == self.player:
                return -10

        # right diagonal
        right = 0
        if board[right + 4][right] == board[right + 2][right + 2] and board[right + 2][right + 2] == board[right][right + 4]:
            if board[right][right] == self.bot:
                return 10
            elif board[right][right] == self.player:
                return -10

        return 0

    def minimax(self, board, depth, is_maximum):
        score = self.evaluate_board(board)
        if score == 1 or score == -1:
            return score

        if not self.check_moves(board):
            return 0

        if is_maximum:
            best = -10
            for i in range(0, len(board), 2):
                for j in range(0, len(board), 2):
                    if type(board[i][j]) == int:
                        temp = board[i][j]
                        board[i][j] = self.bot
                        best = max(best, self.minimax(board, depth + 1, not is_maximum))
                        board[i][j] = temp
            return best
        else:
            best = 10
            for i in range(0, len(board), 2):
                for j in range(0, len(board), 2):
                    if type(board[i][j]) == int:
                        temp = board[i][j]
                        board[i][j] = self.player
                        best = min(best, self.minimax(board, depth + 1, not is_maximum))
                        board[i][j] = temp
            return best

    def find_best_move(self, board):
        best_value = -100
        best_move = (-1, -1)
        for i in range(0, len(board), 2):
            for j in range(0, len(board), 2):
                if type(board[i][j]) == int:
                    temp = board[i][j]
                    board[i][j] = self.bot
                    move = self.minimax(board, 0, False)
                    board[i][j] = temp
                    if move > best_value:
                        best_move = (i, j)
                        best_value = move
        return best_move

    def player_turn(self, board):
        print('Your turn!')
        self.display_board(board)
        temp = input('Choose between 1-9 from the board: ')
        try:
            player_input = int(temp)
            for i in range(0, len(board), 2):
                for j in range(0, len(board), 2):
                    if type(board[i][j]) == int:
                        if board[i][j] == player_input:
                            board[i][j] = self.player
                            print(f'You put {self.player} on board number {player_input}!\n')
                            score = self.evaluate_board(board)
                            if score != 0:
                                self.redo = not self.redo
                                print('You win!')
        except ValueError:
            print('Choose only number from the board!')

    def bot_turn(self, board):
        print('Bot turn!')
        self.display_board(board)
        best_move = self.find_best_move(board)
        row = best_move[0]
        col = best_move[1]
        number = board[row][col]
        if type(board[row][col]) == int:
            board[row][col] = self.bot
            print(f'Bot put {self.bot} on board number {number}!\n')

    def start(self, board):
        self.header()
        if self.player == 'x':
            while self.redo:
                self.player_turn(board)
                self.bot_turn(board)
        elif self.player == 'o':
            while True:
                self.bot_turn(board)
                self.player_turn(board)

if __name__ == '__main__':
    player, bot = '', ''
    board = [
        [1, '|', 2, '|', 3],
        ['-', '+', '-', '+', '-'],
        [4, '|', 5, '|', 6],
        ['-', '+', '-', '+', '-'],
        [7, '|', 8, '|', 9]
    ]

    while player == '':
        player = input('Choose between X or O: ')
        if player.lower() != 'x' and player.lower() != 'o':
            print('Choose only between X or O!')
            player = ''
        else:
            if player.lower() == 'x':
                bot = 'o'
            elif player.lower() == 'o':
                bot = 'x'
    tic = Tictactoe(player.lower(), bot.lower())
    tic.start(board)