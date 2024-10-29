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
    
    numx = 0
    numo = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                numx += 1   
            if board[i][j] == O:
                numo += 1
                
    if numx == numo:
        return X
    else:
        return O

def actions(board):
    
    ans = []
    for row in range(3):
        for col in range(3):
            if (board[row][col] == EMPTY):
                ans.append((row, col))

    return ans

def result(board, action):
    import copy
    ans = copy.deepcopy(board)
    i, j = action
    ans[i][j] = X if player(board) == X else O

    return ans

def winner(board):
    
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] == 'X':
            return X
        if board[row][0] == board[row][1] == board[row][2] == 'O':
            return O
    
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == 'X':
            return X
        if board[0][col] == board[1][col] == board[2][col] == 'O':
            return O

    if board[0][0] == board[1][1] == board[2][2] == 'X':
        return X
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        return O
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        return X
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        return O
    
    return None

def terminal(board):
    
    if winner(board) == X or winner(board) == O:
        return True
    else:
        for row in range(3):
            for col in range(3):
                if (board[row][col] == EMPTY):
                    return False
        return True

def utility(board):
    
    ans = winner(board)
    if ans == X:
        return 1
    else:
        return -1 if ans == O else 0

def minimax(board):
    
    def minValue(board):
        if terminal(board):
            return utility(board)
        res = math.inf
        for action in actions(board):
            res = min(res, maxValue(result(board, action)))
        return res
    
    def maxValue(board):
        if terminal(board):
            return utility(board)
        res = -math.inf
        for action in actions(board):
            res = max(res, minValue(result(board, action)))
            
        return res
    
    ans = -math.inf if player(board) == X else math.inf
    move = (-1, -1)
    
    if player(board) == X:
        for action in actions(board):
            if minValue(result(board, action)) >= ans:
                ans = minValue(result(board, action))
                move = action
            
    if player(board) == O:
        for action in actions(board):
            if maxValue(result(board, action)) <= ans:
                ans = maxValue(result(board, action))
                move = action
                            
    return move            