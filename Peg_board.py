class peg_board:
    def __init__(self):
        self.board = [
             [False],
             [False, False],
             [False, False, False],
             [False, False, False, False],
             [False, False, False, False, False]
        ]
    def board_setup(self, empty_space):
        spot = 0
        for i in range(len(self.board)):
            for j in range(i+1):
                if empty_space != spot:
                    self.board[i][j] = True
                spot += 1
        print(self.board)

