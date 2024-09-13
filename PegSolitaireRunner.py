import logging, datetime, Peg_board, Referee
from KinkaidDecorators import log_start_stop_method
from Peg_board import peg_board
import Referee

logging.basicConfig(level=logging.INFO)  # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]

class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing.")
        self.board = Peg_board.peg_board()
        self.ref = Referee.referee(self.board)
    
    @log_start_stop_method
    def play_game(self):  # note: this is complaining (grey underline) that it could be static because it doesn't use
        # any variables or methods from "self." Once you do, it will stop pestering you about it.
        self.board.board_setup((int)(self.ref.get_hole_pos())-1)
        self.ref.printing_board()
        while True:
            self.ref.run_turn()
            self.ref.printing_board()
            if self.ref.check_end_of_game():
                if self.ref.check_win():
                    print("You win :)")
                else:
                    print("You lost :/")
                break


if __name__ == "__main__":
    game = PegSolitaireRunner()
    game.play_game()

