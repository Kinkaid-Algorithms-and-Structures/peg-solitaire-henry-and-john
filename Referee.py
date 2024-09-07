import Peg_board

class referee:
    def __init__(self, board):
        self.board = board
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
        
                      "              1 \n"
                     f"              {self.board.get_char_at_index(0)} \n"
                    "             2/ \\3 \n"
                   f"            {self.board.get_char_at_index(1)} — {self.board.get_char_at_index(2)} \n"
                  "           4/ \\5/ \\6 \n"
                 f"           {self.board.get_char_at_index(3)} — {self.board.get_char_at_index(4)} — {self.board.get_char_at_index(5)} \n"
                "         7/ \\8/ \\9/ \\10 \n"
               f"         {self.board.get_char_at_index(6)} — {self.board.get_char_at_index(7)} — {self.board.get_char_at_index(8)} — {self.board.get_char_at_index(9)} \n"
             "       11/\\12/\\13/\\14/\\15 \n"
             f"       {self.board.get_char_at_index(10)} — {self.board.get_char_at_index(11)} — {self.board.get_char_at_index(12)} — {self.board.get_char_at_index(13)} — {self.board.get_char_at_index(14)} ")

    def run_turn(self):
        while True:
            start_index = (int) (input("Where is the peg that you want to move? "))
            end_index = (int) (input("Where do you want the peg to go? "))
            if self.board.make_move(start_index-1, end_index-1):
                print("move made")
                return True
            else:
                print("illegal move")