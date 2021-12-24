board = input()
flag = None
if 'X' not in board:
    flag = True
board = board.split('.')
print(board)
ans = ''
while board:
    piece = board.pop(0)
    if piece == '':
        ans += '.'
    else:
        if len(piece)%2 == 1:
            print(-1)
            exit(0)
        else:
            _rest = len(piece)%4
            _quotient = _rest//2
            ans += ('AAAA'*(len(piece)//4) + 'BB' * _quotient)
            if len(board) >= 1:
                if len(board[0]) >= 2:
                    ans += '.'
                if len(board) >= 2:
                    if len(board[1]) >= 2:
                        ans += '.'

if flag:
    print(ans[1:])
else:
    print(ans)

