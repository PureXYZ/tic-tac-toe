from board import Board, GameState
import random


class MiniMax:
    __depth = 10
    player_dict = {1: 'X', -1: 'O'}

    def __evaluate(self, board, depth, player):
        if player == 1:
            player = 'X'
        else:
            player = 'O'

        gs = board.get_gamestate()
        if gs == GameState.X_WIN:
            if player == 'X':
                return 10 - depth
            else:
                return depth - 10
        elif gs == GameState.O_WIN:
            if player == 'O':
                return 10 - depth
            else:
                return depth - 10
        return 0

    def __negamax(self, board, depth, player):
        gs = board.get_gamestate()
        if gs != GameState.NOT_FINISHED:
            return self.__evaluate(board, depth, player)

        best_value = -100

        moves = board.get_valid_moves()
        for move in moves:
            z = Board(board)
            z.make_move(move, self.player_dict[player])
            v = -self.__negamax(z, depth - 1, -player)
            best_value = max(best_value, v)
        return best_value

    # player = 1 is X, -1 is O
    def get_best_move(self, board, player):
        moves = board.get_valid_moves()

        best_score = -100

        scores = []
        best_moves = []

        for move in moves:
            z = Board(board)
            z.make_move(move, self.player_dict[player])
            v = -self.__negamax(z, self.__depth - 1, -player)
            scores.append((move, v))
            best_score = max(best_score, v)

        for score in scores:
            if score[1] == best_score:
                best_moves.append(score[0])

        return(random.choice(best_moves))
