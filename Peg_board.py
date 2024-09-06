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
        # for i in range(15):
        #     print(self.convert_index_to_coords(i))
        coords = self.convert_index_to_coords(empty_space)
        print(coords)
        self.board[coords[1]][coords[0]] = False

    # returns true if the move went through, returns false otherwise
    def make_move(self, start_index, end_index):
        start_pos = self.convert_index_to_coords(start_index)
        end_pos = self.convert_index_to_coords(end_index)
        mid_pos = (((start_pos[0] + end_pos[0]) / 2),
                   ((start_pos[1] + end_pos[1]) / 2))
        if self.is_move_legal(start_pos, mid_pos, end_pos):
            self.board[start_pos[1]][start_pos[0]] = False
            self.board[end_pos[1]][end_pos[0]] = True
            self.board[mid_pos[1]][mid_pos[0]] = False
            return True
        return False

    # turns a given index into 2 indices that can be used to access locations on the board
    # outputs a tuple of (x, y)

    def convert_index_to_coords(self, index):
        x_pos = (index - self.length_formula(self.y_formula(index)))
        # print(self.length_formula(self.y_formula(index)))
        y_pos = self.y_formula(index)
        return x_pos, y_pos

    # returns an index from board coordinates if you ever need that
    def convert_coords_to_index(self, x_pos, y_pos):
        return self.length_formula(y_pos) + x_pos

    # returns the total length to list n in board
    # ex. if n = 3, this will return the lengths of lists 2, 1, and 0, equalling 6
    def length_formula(self, n):
        return (int)(((n ** 2) + n) / 2)

    # returns the y position of a given index in board
    # inverse of length_formula
    def y_formula(self, index):
        return math.floor(math.sqrt((2 * index) + .25) - .5)

    def is_move_legal(self, start_pos, mid_pos, end_pos):
        # check if distance between start and end are either 2 or 4 (the only legal distances)
        if abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1]) != 2 and \
                abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1]) != 4:
            return False
        #  check if the pegs are in the correct spots for a jump
        if not self.board[start_pos[1]][start_pos[0]] or not self.board[mid_pos[1]][mid_pos[0]] or \
                self.board[end_pos[1]][end_pos[0]]:
            return False
        return True
