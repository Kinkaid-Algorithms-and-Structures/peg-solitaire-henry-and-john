import Peg_board
import math

class referee:
    def __init__(self, board):
        self.board = board
        self.move_counter = 0
    def get_hole_pos(self):
        choices = ['1', '2', '3', '4','5','6','7','8','9','10','11','12','13','14','15']
        print("here is the board!\n"
    
              "               1 \n"
              "               o \n"
              "             2/ \\3 \n"
              "             o — o \n"
              "           4/ \\5/ \\6 \n"
              "           o — o — o \n"
              "         7/ \\8/ \\9/ \\10 \n"
              "         o — o — o — o \n"
              "       11/\\12/\\13/\\14/\\15 \n"
              "       o — o — o — o — o ")
        user_choice = input("Enter a hole to leave empty.").lower()

        while user_choice not in choices:
            user_choice = input("Invalid choice.").lower()
        return user_choice
        print(user_choice," Is the position sected to have an empty hole.")

    def printing_board(self):
        print("here is the board!\n"
        
                      "               1 \n"
                     f"               {self.board.get_char_at_index(0)} \n"
                    "             2/ \\3 \n"
                   f"             {self.board.get_char_at_index(1)} — {self.board.get_char_at_index(2)} \n"
                  "           4/ \\5/ \\6 \n"
                 f"           {self.board.get_char_at_index(3)} — {self.board.get_char_at_index(4)} — {self.board.get_char_at_index(5)} \n"
                "         7/ \\8/ \\9/ \\10 \n"
               f"         {self.board.get_char_at_index(6)} — {self.board.get_char_at_index(7)} — {self.board.get_char_at_index(8)} — {self.board.get_char_at_index(9)} \n"
             "       11/\\12/\\13/\\14/\\15 \n"
             f"       {self.board.get_char_at_index(10)} — {self.board.get_char_at_index(11)} — {self.board.get_char_at_index(12)} — {self.board.get_char_at_index(13)} — {self.board.get_char_at_index(14)} ")

    def run_turn(self):
        # not actually an infinite loop because it returns when the player makes a legal move (ik its suspicious code)
        while True:
            start_index = (int) (input("Where is the peg that you want to move? "))
            end_index = (int) (input("Where do you want the peg to go? "))
            if self.board.make_move(start_index-1, end_index-1):
                self.move_counter += 1
                print("move made")
                return True
            else:
                print("illegal move")

    def check_end_of_game(self):
        for i in range(15):
            start_pos = self.board.convert_index_to_coords(i)
            # radians
            for j in range(8):
                rad = j * math.pi / 4
                # always rounds to one when the angle is at pi/4 radians or some equivalent
                # accesses all possible points the peg could move to
                x_offset = 2 * int(round(math.cos(rad)))
                y_offset = 2 * int(round(math.sin(rad)))
                # print(f"{x_offset=}, {y_offset=}")
                end_pos = (start_pos[0]+x_offset, start_pos[1]+y_offset)
                mid_pos = (int((start_pos[0] + end_pos[0]) / 2),
                           int((start_pos[1] + end_pos[1]) / 2))
                # print(f"{start_pos=}, {end_pos=}")
                if self.board.is_move_legal(start_pos, mid_pos, end_pos):
                    return False
        return True

    def check_win(self):
        # there are 14 pegs to start, and you win when there is only one on the board
        # each move, one peg is removed and the move counter increments by one,
        # so you win if there are no legal moves but the counter is at 13
        if self.move_counter == 13:
            return True
        return False
