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

    # returns the value at an index in the board (boolean)
    def get_value_at_index(self, index):
        pos = self.convert_index_to_coords(index)
        return self.board[pos[1]][pos[0]]
    def get_char_at_index(self, index):
        if self.get_value_at_index(index):
            return "ø"
        else:
            return "o"
    def board_setup(self, empty_space):
        # for i in range(15):
        #     print(self.convert_index_to_coords(i))
        coords = self.convert_index_to_coords(empty_space)
        # print(coords)
        self.board[coords[1]][coords[0]] = False

    # returns true if the move went through, returns false otherwise
    def make_move(self, start_index, end_index):
        start_pos = self.convert_index_to_coords(start_index)
        end_pos = self.convert_index_to_coords(end_index)
        mid_pos = ((int)((start_pos[0] + end_pos[0]) / 2),
                   (int)((start_pos[1] + end_pos[1]) / 2))
        # print(f"{start_pos=}, {mid_pos=}, {end_pos=}")
        if self.is_move_legal(start_pos, mid_pos, end_pos, True):
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

    def is_move_legal(self, start_pos, mid_pos, end_pos, print_reason):
        # print(f"{start_pos=}, {end_pos=}")
        # checks if the start or end are out of bounds.
        # no need to check the middle because if the middle is out of bounds, one of the others is out of bounds.
        if start_pos[0] > start_pos[1] or start_pos[0] < 0 or end_pos[0] > end_pos[1] or end_pos[0] < 0 or \
                start_pos[1] > 4 or start_pos[1] < 0 or end_pos[1] > 4 or end_pos[1] < 0:
            if print_reason:
                print("out of bounds")
            return False
        # check if distance between x positions are 0 or 2 and if difference between y positions are 0 or 2,
        # and also checks if the start and end are the same
        if abs(start_pos[0] - end_pos[0]) != 0 and abs(start_pos[0] - end_pos[0]) != 2 and \
                abs(start_pos[1] - end_pos[1]) != 0 and abs(start_pos[1] - end_pos[1]) != 2 or \
                start_pos == end_pos:
            if print_reason:
                print("illegal end position")
            return False
        # if the offsets are (+2, +2) or (-2, -2), then the move is actually illegal, but they get past the if statement above

        if -1 * (start_pos[0]-end_pos[0]) == start_pos[1]-end_pos[1]:
            if print_reason:
                print("forbidden diagonal jump")
            return False
        #  check if the pegs are in the correct spots for a jump
        if (not self.board[start_pos[1]][start_pos[0]]) or (not self.board[mid_pos[1]][mid_pos[0]]) or \
                (self.board[end_pos[1]][end_pos[0]]):
            if print_reason:
                print("pegs not in right spots")
            return False
        return True
