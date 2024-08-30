# Chess Board Validator

chess_board_keys = []

for number in range(1, 9):
    for character in range(97, 105):
        chess_board_keys.append(chr(character) + str(number))

valid_pieces = ['wking', 'wqueen', 'wrook', 'wrook', 'wbishop', 'wbishop', 
                'wknight', 'wknight', 'wpawn', 'wpawn', 'wpawn', 'wpawn',
                'wpawn', 'wpawn', 'wpawn', 'wpawn', 'bking', 'bqueen',
                'brook', 'brook', 'bbishop', 'bbishop', 
                'bknight', 'bknight', 'bpawn', 'bpawn', 'bpawn', 'bpawn',
                'bpawn', 'bpawn', 'bpawn', 'bpawn', ]

board = {}

for i in range(len(valid_pieces)):
    board.setdefault(chess_board_keys[i], valid_pieces.pop())


def is_valid_chess_board(board):
    """Validate counts and location of pieces on board"""

    chess_board_keys = []
    for number in range(1, 9):
        for character in range(97, 105):
           chess_board_keys.append(chr(character) + str(number))
    
    pieces = ['king','queen','rook', 'knight','bishop', 'pawn']
    colors = ['b', 'w']
    all_pieces = set(color+piece for piece in pieces for color in colors)
    
    valid_piece_counts = {'king': (1, 1),
                          'queen': (0, 1),
                          'rook': (0, 2),
                          'bishop': (0, 2),
                          'knight': (0, 2),
                          'pawn': (0, 8)}
    
    piece_count = {}
    for v in board.values():
       if v in all_pieces:
        piece_count.setdefault(v, 0)
        piece_count[v] += 1
    
    for piece in all_pieces:
        count = piece_count.get(piece, 0)
        low, high = valid_piece_counts[piece[1:]]
        if not low <= count <= high:
            if low != high:
               print(f'There should between {low} and {high} {piece} but there are {count}')
            else:
               print(f'There should be {low} {piece} but there are {count})')
            return False
    
    for location in board.keys():
        row = int(location[1:])
        column = location[:1]
        if not ((1 <= row <= 8) and ('a' <= column <= 'h')):
          print(f'Invalid to have {board[location]} at postion {location}')
          return False

    for location, piece in board.items():
       if piece:
          if not piece in all_pieces:
            print(f'{piece} is not a valid chess piece at postion {location}')
            return False

    print('Board OK')
    return True

is_valid_chess_board(board)