from square import Square
from enum import Enum


class GameState(Enum):
    X_WIN = 1
    O_WIN = 2
    TIE = 3
    NOT_FINISHED = 4


class Board:
    __move_index = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                    '4': (1, 0), '5': (1, 1), '6': (1, 2),
                    '7': (2, 0), '8': (2, 1), '9': (2, 2)}

    __rows_index = [0, 1, 2]
    __BOARD_SIZE = 3

    def __init__(self, board=None):
        self.__rows = [[Square('None'), Square('None'), Square('None')],
                       [Square('None'), Square('None'), Square('None')],
                       [Square('None'), Square('None'), Square('None')]]

        self.__last_move = None

        if board:
            for k in self.__move_index:
                p = board.get_square(k)
                if p:
                    self.__set_square(k, p)
            self.__last_move = board.get_last_move()

    def get_last_move(self):
        return self.__last_move

    def __set_square(self, index, piece):
        if index in self.__move_index:
            x = self.__move_index[index][0]
            y = self.__move_index[index][1]
            self.__rows[x][y].set_piece(piece)
        else:
            raise ValueError('Invalid Set Move Index')

    def get_square(self, index):
        if index in self.__move_index:
            x = self.__move_index[index][0]
            y = self.__move_index[index][1]
            return self.__rows[x][y].get_piece()
        else:
            raise ValueError('Invalid Get Move Index')

    def make_move(self, index, piece):
        self.__set_square(index, piece)
        self.__last_move = index

    def get_valid_moves(self):
        moves = []
        for key in self.__move_index:
            if self.get_square(key) is None:
                moves.append(key)
        return moves

    def __three_in_a_row(self, piece, x, y):
        h = 0
        v = 0
        diag = 0
        anti_diag = 0

        for i in self.__rows_index:
            if self.__rows[i][y].get_piece() == piece:
                h += 1
            if self.__rows[x][i].get_piece() == piece:
                v += 1
            if self.__rows[i][i].get_piece() == piece:
                diag += 1
            if self.__rows[self.__BOARD_SIZE - i - 1][i].get_piece() == piece:
                anti_diag += 1

        return h == 3 or v == 3 or diag == 3 or anti_diag == 3

    # None if no winner, else game state
    def __is_winner(self, last_move):
        if last_move is None:
            return None

        # check last_move row and column for three in a row
        x = self.__move_index[last_move][0]
        y = self.__move_index[last_move][1]
        piece = self.__rows[x][y].get_piece()

        win = self.__three_in_a_row(piece, x, y)

        if win:
            if piece == 'X':
                return GameState.X_WIN
            else:
                return GameState.O_WIN

        return None

    def get_gamestate(self):
        if self.__last_move:
            win = self.__is_winner(self.__last_move)
        else:
            return GameState.NOT_FINISHED

        if win:
            return win
        elif not win and not self.get_valid_moves():
            return GameState.TIE

        return GameState.NOT_FINISHED

    def print_debug(self):
        print('==========================')
        for i in self.__rows_index:
            for j in self.__rows_index:
                p = self.__rows[i][j].get_piece()
                if p is None:
                    p = '_'
                print('( ' + str(i) + ', ' + str(j) + '): ' + p + ' ', end='')
            print()
        print(self.get_gamestate())
        print('Last move: ' + str(self.get_last_move()))
        print('==========================')
