class Square:
    __piece_dict = {'X': 'X', 'O': 'O', 'None': None}

    def __init__(self, piece):
        self.__piece = None

        if piece in self.__piece_dict:
            self.__piece = self.__piece_dict[piece]
        else:
            raise ValueError('Wrong Piece')

    def get_piece(self):
        return self.__piece

    def set_piece(self, piece):
        valid = piece != 'None' \
                and piece in self.__piece_dict \
                and self.__piece is None

        if valid:
            self.__piece = self.__piece_dict[piece]
        else:
            raise ValueError('Invalid Move')
