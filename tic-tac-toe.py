from board import Board, GameState
from minimax import MiniMax

b = Board()
mm = MiniMax()
player = 1


while(b.get_gamestate() == GameState.NOT_FINISHED):
	if player == 1:
		pass
	else:
		move = mm.get_best_move(b, player)
		
	while True and player == 1:
		move = input('Enter move (1 - 9): ')
		try:
			b.make_move(move, mm.player_dict[player])
		except ValueError:
			print('Dumbass')
		else:
			break

	b.print_debug()
	
	player = -player
	
	
"""
while(b.get_gamestate() == GameState.NOT_FINISHED):
	move = mm.get_best_move(b, player)
	b.make_move(move, mm.player_dict[player])

	b.print_debug()
	
	player = -player
"""
