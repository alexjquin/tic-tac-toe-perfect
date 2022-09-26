import random

PLAYER = "PLAYER"
AI = "AI"


class Board:
    def __init__(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]
        self.active_turn = random.choice([AI])

    def play(self, index) -> bool:
        if self.active_turn == PLAYER:
            self.board[index] = "X"
            self.active_turn = AI
        else:
            self.board[index] = "O"
            self.active_turn = PLAYER

        return True

    # Returns (bool, bool/None)
    # First item is if game is over, True/False
    # Second item is True for player win, False for AI win or None if tie or game is not over
    def check_result(self):
        # horizontal wins
        if (self.board[0] != " ") and self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            return True, self.board[0] == "X",

        elif (self.board[3] != " ") and self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            return True, self.board[3] == "X"

        elif (self.board[6] != " ") and self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            return True, self.board[6] == "X"

        # vertical wins
        elif (self.board[0] != " ") and self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            return True, self.board[0] == "X"

        elif (self.board[1] != " ") and self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            return True, self.board[1] == "X"

        elif (self.board[2] != " ") and self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            return True, self.board[2] == "X"

        # diagonal wins
        elif (self.board[0] != " ") and self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            return True, self.board[0] == "X"

        elif (self.board[6] != " ") and self.board[6] == self.board[4] and self.board[4] == self.board[2]:
            return True, self.board[6] == "X"

        elif len(self.get_available_moves()) == 0:
            return True, None

        return False, None

    def get_available_moves(self) -> list:
        return [index for index, spot in enumerate(self.board) if spot == " "]

    def get_new_state(self, move):
        new_state = Board()
        new_state.copy_board(self)
        new_state.active_turn = self.active_turn
        new_state.play(move)

        return new_state

    def copy_board(self, board):
        self.board = [item for item in board.board]
        if board.active_turn == PLAYER:
            self.active_turn = PLAYER
        else:
            self.active_turn = AI
