import board


def move_score(game_board, depth):
    result = game_board.check_result()[1]
    if result is None:
        return 0
    # if AI won, return max score
    elif not result:
        return 10 - depth
    # if player won, return min score
    elif result:
        return depth - 10


class MiniMax:
    def __init__(self):
        self.choice = -1

    def minimax(self, game_board: board.Board, depth: int) -> int:
        if game_board.check_result()[0]:
            return move_score(game_board, depth)

        depth += 1
        scores = []  # an array of scores
        moves = []  # an array of moves

        # Populate the scores array, recursing as needed
        for move in game_board.get_available_moves():
            possible_game = game_board.get_new_state(move)
            score = self.minimax(possible_game, depth)
            scores.append(score)
            moves.append(move)

        # Do the min or the max calculation

        if game_board.active_turn == "AI":
            # This is the max calculation
            max_score_index = scores.index(max(scores))
            self.choice = moves[max_score_index]
            return scores[max_score_index]
        else:
            # This is the min calculation
            min_score_index = scores.index(min(scores))
            self.choice = moves[min_score_index]
            return scores[min_score_index]
