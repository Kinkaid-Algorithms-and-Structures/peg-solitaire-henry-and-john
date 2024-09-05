import math

class peg_board:
    def __init__(self):
        self.board = [
             [True],
             [True, True],
             [True, True, True],
             [True, True, True, True],
             [True, True, True, True, True]
        ]
    def board_setup(self, empty_space):
        coords = self.convert_index_to_coords(empty_space)
        print(coords)
        self.board[coords[1]][coords[0]] = False
        print(self.board)
    #when moving up, move the same amount to the left
    #when moving down, move the same amount to the right
    def make_move(self, start_index, end_index):
        start_pos = self.convert_index_to_coords(start_index)
        end_pos = self.convert_index_to_coords(end_index)
        self.board[start_pos[1]][start_pos[0]] = False
        self.board[end_pos[1]][end_pos[0]] = True
        # not complete, needs to access the point being jumped over

    # turns a given index into 2 indices that can be used to access locations on the board
    # outputs a tuple of (x, y)
    def convert_index_to_coords(self, index):
        x_pos = (index - self.length_formula(self.y_formula(index)))
        print(self.length_formula(self.y_formula(index)))
        y_pos = self.y_formula(index)
        return x_pos, y_pos

    # returns an index from board coordinates if you ever need that
    def convert_coords_to_index(self, x_pos, y_pos):
        return self.length_formula(y_pos) + x_pos

    # returns the total length to list n in board
    # ex. if n = 3, this will return the lengths of lists 2, 1, and 0, equalling 6
    def length_formula(self, n):
        return (int)(((n ** 2) + n)/2)

    # returns the y position of a given index in board
    # inverse of length_formula
    def y_formula(self, index):
        return math.floor(math.sqrt((2*index)+.25)-.5)

