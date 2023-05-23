import time

from reversi import *
from minmax import *
from evaluateHeuristics import *
from AIPlayer import *


def main():
    game_mode = choose_players()

    if game_mode != 2:  # AI is involved
        print("Choose evaluation method for AI Player 1 (X):")
        eval_method1 = choose_evaluation_method()
        if eval_method1 == 1:
            ai_player1 = AIPlayer(lambda game: based_on_board_pieces(game.board))
        elif eval_method1 == 2:
            ai_player1 = AIPlayer(lambda game: based_on_board_moves(game))
        elif eval_method1 == 3:
            ai_player1 = AIPlayer(lambda game: based_on_board_flipped_pieces(game))

        if game_mode == 3:  # AI vs AI
            print("Choose evaluation method for AI Player 2 (O):")
            eval_method2 = choose_evaluation_method()
            if eval_method2 == 1:
                ai_player2 = AIPlayer(lambda game: based_on_board_pieces(game.board))
            elif eval_method2 == 2:
                ai_player2 = AIPlayer(lambda game: based_on_board_moves(game))
            elif eval_method2 == 3:
                ai_player2 = AIPlayer(lambda game: based_on_board_flipped_pieces(game))

    game = Reversi()
    time_performed = 0
    start = 0
    end = 0
    current_move_counter = 0
    while True:
        valid_moves = game.get_valid_moves()
        if not valid_moves:
            if game.current_player == 1:
                break

        print(f"Player {game.current_player}'s turn")
        print_board(game.board)
        print(f"Valid moves: {valid_moves}")

        if game_mode == 1 and game.current_player == 2 or game_mode == 3:
            ai_turn = True
        else:
            ai_turn = False

        if ai_turn:
            start = time.time()
            if game.current_player == 1:
                ai_player = ai_player1
                minmax = True
            else:
                ai_player = ai_player2 if game_mode == 3 else ai_player1
                minmax = False

            best_move = None
            best_eval = float('-inf')
            if current_move_counter > 30:
                depth = 4
            else:
                depth = 4

            alpha = float('-10')
            beta = float('10')
            for move in valid_moves:
                new_game = copy.deepcopy(game)
                new_game.make_move(*move)
                # evaluate = minimax(new_game, ai_player, depth, minmax)
                evaluate = minimax_alpha_beta(new_game, ai_player, depth, alpha, beta, minmax)
                if evaluate > best_eval:
                    best_eval = evaluate
                    best_move = move
            row, col = best_move
            end = time.time()
        else:
            good_to_go = False
            while not good_to_go:
                try:
                    row, col = map(int, input("Enter row and column: ").split())
                    if (row, col) in valid_moves:
                        good_to_go = True
                except ValueError:
                    pass

        if (row, col) in valid_moves:
            print(f'({row},{col})')
            game.make_move(row, col)
            current_move_counter += 1
            time_performed += end - start
            print(f'time: {end - start}')
            if game.current_player == 1:
                print(f'current move: {current_move_counter / 2}')
        else:
            print("Invalid move try again")
            game.current_player = 3 - game.current_player

    print_board(game.board)
    winner = game.get_winner()
    print(time_performed)
    if winner == 0:
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")


def print_board(board):
    print("   0 1 2 3 4 5 6 7 ")
    print("  +-+-+-+-+-+-+-+-+")
    for row in range(8):
        print(row, end=" |")
        for col in range(8):
            if board[row][col] == 0:
                print(" ", end="|")
            elif board[row][col] == 1:
                print("X", end="|")
            else:
                print("O", end="|")
        print("\n  +-+-+-+-+-+-+-+-+")


def choose_players():
    print("Choose game mode:")
    print("1. Human vs AI")
    print("2. Human vs Human")
    print("3. AI vs AI")

    choice = int(input("Enter the number (1, 2, or 3): "))
    while choice not in [1, 2, 3]:
        choice = int(input("Invalid choice, enter the number (1, 2, or 3): "))

    return choice


if __name__ == "__main__":
    main()
