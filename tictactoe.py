"""
Tic Tac Toe Player
"""

import math

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
    if terminal(board) == True:
        return None    
    countO, countX = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1
    if countO >= countX:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsSet = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] != O and board[i][j] != X:
                actionsSet.add((i, j))
    return actionsSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # valid action: if action is a tuple and 0 <= i, j <=2.
    if type(action) != tuple or (action[0] >= 3 or action[0] < 0 or action[1] >= 3 or action[1] < 0):
        raise ValueError("Not a valid action for the board")
    # copying board
    board_copy = [[], [], []]
    for i in range(3):
        for j in range(3):
            board_copy[i].append(board[i][j])
    turn = player(board)
    if turn == None:
        return board_copy
    else:
        board_copy[action[0]][action[1]] = turn
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check columns
    for j in range(3):
        if board[1][j] == board[0][j] and board[0][j] == board[2][j] and board[1][j] != EMPTY:
            return board[1][j]
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
    # check diagnols
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[1][1]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    ended = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                ended = False
    return ended


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    elif player(board) == X:
        action = maxit(board)[1:]
    elif player(board) == O:
        action = minit(board)[1:]
    return action


def maxit(board):
    """
    Return tuple (utility, i, j) where (i, j) represents the move with
    the maximum utility and utility represents that maximum utility,
    given the board board.
    """
    maxval = -2

    row_index = None
    col_index = None
    # if terminal board, terminate the function.
    if terminal(board) == True:
        result = utility(board)
        return (result, 0, 0)    
    # for each possible move, calculate its utility, saving the maximum.
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                board[i][j] = X
                (m, mini, minj) = minit(board)
                if m > maxval:
                    maxval=m
                    row_index=i
                    col_index=j
                board[i][j] = EMPTY
    return (maxval, row_index, col_index)


def minit(board):
    """
    Return tuple (utility, i, j) where (i, j) represents the move with
    the minimum utility and utility represents that minimum utility,
    given the board board.
    """
    minval = 2

    row_index = None
    col_index = None
    # if terminal board, terminate the function.
    if terminal(board) == True:
        result = utility(board)
        return (result, 0, 0)
    # for each possible move, calculate its utility, saving the minimum.
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                board[i][j] = O
                (m, maxi, maxj) = maxit(board)
                if m < minval:
                    minval = m
                    row_index = i
                    col_index = j
                board[i][j] = EMPTY

    return (minval, row_index, col_index)
