class Square:

	piece = None
	
	piece_dict = {'X': 'X', 'O': 'O', 'None': None}

	def __init__(self, piece):
		if piece in self.piece_dict:
			self.piece = self.piece_dict[piece]
		else:
			raise ValueError('Wrong Piece')
	
	def get_piece(self):
		return self.piece
	
	def set_piece(self, piece):
		valid = piece != 'None' and piece in piece_dict and self.piece is None
		
		if valid:
			self.piece = piece_dict[piece]
		else:
			raise ValueError('Invalid Move')