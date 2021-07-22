n = int(input())
cnt = 0
move = []
def hanoi_tower(n,l = 1,m =2,r = 3):
    global cnt
    if n == 0:
        return
    hanoi_tower(n-1,l,r,m)
    move.append([l, r])
    cnt += 1
    hanoi_tower(n-1,m,l,r)


hanoi_tower(n)
print(cnt)
for item in move:
    x, y = item
    print(x,y)