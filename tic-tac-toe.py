from board import Board, GameState
from minimax import MiniMax

b = Board()
mm = MiniMax()

player_dict = mm.player_dict

b.print_debug()

player = 1

move = mm.get_best_move(b, player)

b.make_move(move, player_dict[player])

b.print_debug()

player = -player

move = mm.get_best_move(b, player)

b.make_move(move, player_dict[player])

b.print_debug()
