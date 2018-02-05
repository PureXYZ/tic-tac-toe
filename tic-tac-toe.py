from board import Board, GameState

b = Board()
b.print_debug()
b.make_move('1', 'O')
b.make_move('5', 'O')
b.make_move('9', 'O')
b.print_debug()
c = Board(b)
c.print_debug()