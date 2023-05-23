def based_on_board_moves(game):
    current_player_moves = len(game.get_valid_moves())
    game.current_player = 3 - game.current_player

    opponent_moves = len(game.get_valid_moves())
    game.current_player = 3 - game.current_player

    return current_player_moves - opponent_moves


def based_on_board_pieces(board):
    counts = [0, 0, 0]
    for row in range(8):
        for col in range(8):
            counts[board[row][col]] += 1
    return counts[1] - counts[2]


def based_on_board_flipped_pieces(game):
    valid_moves = game.get_valid_moves()
    flipped_pieces = [game.flipped_pieces(row, col) for row, col in valid_moves]
    return sum(flipped_pieces)
