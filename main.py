class Tictactoe:
    player, bot = '', ''

    def __init__(self, player, bot):
        self.player = player
        self.bot = bot

    def display_board(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                print(board[i][j], end='')
            print('')

    def available_moves(self, board, number):
        for i in range(0, len(board), 2):
            for j in range(0, len(board[i]), 2):
                if type(board[i][j]) == int:
                    if board[i][j] == number:
                        return True
        return False

    def get_number_position(self, board, number):
        for i in range(0, len(board), 2):
            for j in range(0, len(board[i]), 2):
                if board[i][j] == number:
                    return (i, j)
        return (-1, -1)

    def tie(self, board):
        for i in range(0, len(board), 2):
            for j in range(0, len(board[i]), 2):
                if type(board[i][j]) == int:
                    return False
        return True

    def evaluate_board(self, board, label=''):
        #check row
        for i in range(0, len(board), 2):
            if board[i][0] == board[i][2] and board[i][2] == board[i][4]:
                return True
            if board[i][0] == board[i][2] and board[i][2] == board[i][4] and board[i][0] == label:
                return True

        #check column
        for i in range(0, len(board), 2):
            if board[0][i] == board[2][i] and board[2][i] == board[4][i]:
                return True
            if board[0][i] == board[2][i] and board[2][i] == board[4][i] and board[0][i] == label:
                return True

        #left diagonal
        if board[0][0] == board[2][2] and board[2][2] == board[4][4]:
            return True
        if board[0][0] == board[2][2] and board[2][2] == board[4][4] and board[0][0] == label:
            return True

        #right diagonal
        if board[4][0] == board[2][2] and board[2][2] == board[0][4]:
            return True
        if board[4][0] == board[2][2] and board[2][2] == board[0][4] and board[4][0] == label:
            return True
        return False

    def put_label(self, board, number, label):
        if self.available_moves(board, number):
            x, y = self.get_number_position(board, number)
            board[x][y] = label
            self.display_board(board)
            if self.tie(board):
                print("=== TIE ===")
                exit()
            if self.evaluate_board(board):
                if label == self.player:
                    print("=== YOU WIN ===")
                    exit()
                elif label == self.bot:
                    print("=== AI WIN ===")
                    exit()
            return
        else:
            print(f"Cant put label on number {number}")
            number = int(input("Enter new position: "))
            self.put_label(board, number, label)
            return

    def minimax(self, board, depth, is_maximum):
        if self.evaluate_board(board, self.bot):
            return 1
        elif self.evaluate_board(board, self.player):
            return -1
        elif self.tie(board):
            return 0

        if is_maximum:
            best_score = -1
            for i in range(0, len(board), 2):
                for j in range(0, len(board[i]), 2):
                    if type(board[i][j]) == int:
                        value = board[i][j]
                        board[i][j] = self.bot
                        score = max(best_score, self.minimax(board, depth + 1, False))
                        board[i][j] = value
                        if score > best_score:
                            best_score = score
            return best_score
        else:
            best_score = 1
            for i in range(0, len(board), 2):
                for j in range(0, len(board[i]), 2):
                    if type(board[i][j]) == int:
                        value = board[i][j]
                        board[i][j] = self.player
                        score = min(best_score, self.minimax(board, depth + 1, True))
                        board[i][j] = value
                        if score < best_score:
                            best_score = score
            return best_score

    def player_turn(self, board):
        self.display_board(board)
        position = int(input("Choose between 1-9 from the board: "))
        self.put_label(board, position, self.player)
        return

    def ai_turn(self, board):
        best_score = -1
        best_move = 0
        for i in range(0, len(board), 2):
            for j in range(0, len(board[i]), 2):
                if type(board[i][j]) == int:
                    value = board[i][j]
                    board[i][j] = self.bot
                    score = self.minimax(board, 0, False)
                    board[i][j] = value
                    if score > best_score:
                        best_score = score
                        best_move = value
        self.put_label(board, best_move, self.bot)
        return

    def start(self, board):
        if self.player == 'x'.upper():
            while not self.evaluate_board(board):
                self.player_turn(board)
                self.ai_turn(board)
        elif self.player == 'o'.upper():
            while not self.evaluate_board(board):
                self.ai_turn(board)
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
    tic = Tictactoe(player.upper(), bot.upper())
    tic.start(board)