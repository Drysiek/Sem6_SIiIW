import copy


def minimax(game, ai_player, depth, maximizing_player):
    valid_moves = game.get_valid_moves()
    if depth == 0 or len(valid_moves) < 1:
        return ai_player.evaluate_board(game)

    if maximizing_player:
        best_eval = float('-inf')
        for move in valid_moves:
            new_game = copy.deepcopy(game)
            new_game.make_move(*move)
            evaluate = minimax(new_game, ai_player, depth - 1, False)
            best_eval = max(best_eval, evaluate)
        return best_eval
    else:
        best_eval = float('inf')
        for move in valid_moves:
            new_game = copy.deepcopy(game)
            new_game.make_move(*move)
            evaluate = minimax(new_game, ai_player, depth - 1, True)
            best_eval = min(best_eval, evaluate)
        return best_eval


def minimax_alpha_beta(game, ai_player, depth, alpha, beta, maximizing_player):
    valid_moves = game.get_valid_moves()

    if depth == 0 or len(valid_moves) < 1:
        return ai_player.evaluate_board(game)

    if maximizing_player:
        best_eval = float('-inf')
        for move in valid_moves:
            new_game = copy.deepcopy(game)
            new_game.make_move(*move)
            evaluate = minimax_alpha_beta(new_game, ai_player, depth - 1, alpha, beta, False)
            best_eval = max(best_eval, evaluate)
            alpha = max(alpha, best_eval)
            if beta <= alpha:
                break
        return best_eval
    else:
        best_eval = float('inf')
        for move in valid_moves:
            new_game = copy.deepcopy(game)
            new_game.make_move(*move)
            evaluate = minimax_alpha_beta(new_game, ai_player, depth - 1, alpha, beta, True)
            best_eval = min(best_eval, evaluate)
            beta = min(beta, best_eval)
            if beta <= alpha:
                break
        return best_eval
