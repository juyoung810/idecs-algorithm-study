board = input()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if board.count('X') >= 1:
    board = -1
print(board)