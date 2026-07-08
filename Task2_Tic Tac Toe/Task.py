import math

board = [" "]*9

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in w)

def minimax(is_max):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in board: return 0

    best = -math.inf if is_max else math.inf

    for i in range(9):
        if board[i]==" ":
            board[i] = "O" if is_max else "X"
            score = minimax(not is_max)
            board[i] = " "
            best = max(best, score) if is_max else min(best, score)

    return best

def best_move():
    best, move = -math.inf, -1
    for i in range(9):
        if board[i]==" ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best:
                best, move = score, i
    return move
