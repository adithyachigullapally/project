"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count moves
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    i, j = action
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = []

    # Rows
    lines.extend(board)

    # Columns
    for j in range(3):
        lines.append([board[i][j] for i in range(3)])

    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line == [X, X, X]:
            return X
        if line == [O, O, O]:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    turn = player(board)

    def max_value(state):
        if terminal(state):
            return utility(state)
        v = -math.inf
        for act in actions(state):
            v = max(v, min_value(result(state, act)))
        return v

    def min_value(state):
        if terminal(state):
            return utility(state)
        v = math.inf
        for act in actions(state):
            v = min(v, max_value(result(state, act)))
        return v

    best_action = None

    if turn == X:
        value = -math.inf
        for act in actions(board):
            min_val = min_value(result(board, act))
            if min_val > value:
                value = min_val
                best_action = act
    else:
        value = math.inf
        for act in actions(board):
            max_val = max_value(result(board, act))
            if max_val < value:
                value = max_val
                best_action = act

    return best_action
