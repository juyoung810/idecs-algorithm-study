n = input()
cnt = 0
row = ord(n[0])-ord('a') + 1
col = int(n[1])
loc = [row, col]
movements = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
for move in movements:
    _newloc = [loc[0] + move[0], loc[1] + move[1]]
    if (_newloc[0] > 1 and _newloc[0] <= 8) and (_newloc[1] > 1 and _newloc[1] <= 8):
        cnt += 1

print(cnt)

