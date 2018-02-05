from board import Board, GameState
from minimax import MiniMax



def cvp():
	b = Board()
	mm = MiniMax()
	player = 1
	while(b.get_gamestate() == GameState.NOT_FINISHED):
		if player == 1:
			move = input('Enter move (1 - 9): ')
		else:
			move = mm.get_best_move(b, player)
			
		b.make_move(move, mm.player_dict[player])

		b.print_debug()
		
		player = -player

def cvc():
	b = Board()
	mm = MiniMax()
	player = 1

	while(b.get_gamestate() == GameState.NOT_FINISHED):
		move = mm.get_best_move(b, player)
		b.make_move(move, mm.player_dict[player])

		b.print_debug()
		
		player = -player
		


import cProfile
import re
cProfile.run('cvc()')