import tkinter as tk
import board
import minimax

YOUR_TURN = "Your turn"


class GameUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.board = board.Board()

        self.turn_label = tk.Label(font=("Arial", 20, "bold"))
        self.update_label()
        self.turn_label.grid(row=0, column=0, columnspan=3)

        self.all_buttons = []
        self.unplayed = []

        self.title("Tic Tac Toe")

        btn_index = 0
        for row in range(0, 3):
            for column in range(0, 3):
                # command = lambda index=btn_index: self.play(index)
                button = tk.Button(text=" ",
                                   width=4,
                                   command=lambda index=btn_index: self.on_click(index),
                                   font=("Arial", 50, "bold"))
                self.all_buttons.append(button)
                self.unplayed.append(button)
                button.grid(row=row + 1, column=column)
                btn_index += 1

    def on_click(self, index):
        self.process_player(index)

        game_over, result = self.board.check_result()

        if game_over:
            self.disable_all_buttons()
            if result is None:
                self.turn_label.config(text="Tie game!")
            elif result:
                self.turn_label.config(text="Congratulations, you win!")

        else:
            self.process_ai()

    def process_ai(self):
        self.update_label()
        self.disable_all_buttons()

        ai = minimax.MiniMax()
        ai.minimax(game_board=self.board, depth=0)
        ai_button = self.all_buttons[ai.choice]
        ai_button.config(text="O", state=tk.DISABLED)
        self.board.play(ai.choice)
        self.unplayed.remove(ai_button)

        game_over, result = self.board.check_result()
        if game_over:
            self.disable_all_buttons()
            if result is None:
                self.turn_label.config(text="Tie game!")
            elif not result:
                self.turn_label.config(text="Sorry, you lose")
        else:
            self.enable_unused()
            self.update_label()

    def process_player(self, index):
        button = self.all_buttons[index]
        button.config(text="X", state=tk.DISABLED)
        self.unplayed.remove(button)
        self.board.play(index)

    def disable_all_buttons(self):
        for button in self.unplayed:
            button.config(state=tk.DISABLED)

    def enable_unused(self):
        for button in self.unplayed:
            button.config(state=tk.NORMAL)

    def update_label(self):
        if self.board.active_turn == board.AI:
            self.turn_label.config(text="Thinking...")
        else:
            self.turn_label.config(text=YOUR_TURN)

    def start_game(self):
        if self.board.active_turn == board.AI:
            self.process_ai()
