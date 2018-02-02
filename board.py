from square import Square

class Board:
	rows = [[Square('None'), Square('None'), Square('None')],
			[Square('None'), Square('None'), Square('None')],
			[Square('None'), Square('None'), Square('None')]]
			
	move_index = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
				  '4': (1, 0), '5': (1, 1), '6': (1, 2),
				  '7': (2, 0), '8': (2, 1), '9': (2, 2)}
				  
	def __init__(self, board):
		for key in move_index:
			self.set_square(key, board.get_square(key))
			
	def set_square(self, index, piece):
		x = self.move_index[index][0]
		y = self.move_index[index][1]
		self.rows[x][y].set_piece(piece)
		
	def get_square(self, index):
		x = self.move_index[index][0]
		y = self.move_index[index][1]
		return self.rows[x][y].get_piece()
				  
	def make_move(self, index, piece):
		try:
			self.set_square(index, piece)
		except ValueError:
			pass
		
	def get_valid_moves(self):
		moves = []
		for key in move_index:
			if self.get_square(key) is not None:
				moves.append(key)
		return moves
		
	def is_winner(self):
		pass
			
	def is_tie(self):
		return not self.is_winner() and not self.get_valid_moves()
		
	def is_gameover(self):
		return self.is_winner() or self.is_tie()