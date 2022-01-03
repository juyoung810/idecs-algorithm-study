N = int(input())
n = []
for _ in range(N):
    _x = int(input())
    n.append(_x)
n.sort(reverse = True)
tip=0
for i in range(1, len(n)+1):
    if n[i-1]-(i-1) >=0:
        tip = tip + (n[i-1]-(i-1))
    else:
        tip += 0
print(tip)