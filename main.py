import board
import minimax

game = board.Board()


while not game.check_result()[0]:
    if game.active_turn == board.PLAYER:
        game.print()
        awaiting_valid_move = True
        while awaiting_valid_move:
            choice = int(input("Enter index for next move (0-8): "))
            if game.is_valid_move(choice):
                game.play(choice)
                awaiting_valid_move = False
            else:
                print("Please enter a valid move.")
    else:
        ai = minimax.MiniMax()
        score = ai.minimax(game_board=game, depth=0)
        game.play(ai.choice)

winner = game.check_result()[1]

game.print()
if winner is None:
    print("Tie game!")
elif winner:
    print("Congratulations! You Won!")
else:
    print("Sorry, you lose.")
