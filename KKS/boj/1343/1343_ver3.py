board = input()
ans = ''
counter = 0
def recur_get_first(x):
    global counter
    temp = x[0]
    if x[0] == '.' and counter == 0:
        return temp
    if x[0] == '.' and counter != 0:
        return ''
    if len(x) == 1:
        return temp
    else:
        counter += 1
        return temp + recur_get_first(x[1:])

while board:
    piece = ''
    counter = 0
    piece = recur_get_first(board)
    board = board[len(piece):]
    if piece == '.':
        ans += piece
    else:
        if len(piece) % 2 == 1:
            print(-1)
            exit(0)
        else:
            _rest = len(piece) % 4
            _quotient = _rest // 2
            ans += ('AAAA' * (len(piece) // 4) + 'BB' * _quotient)

print(ans)
