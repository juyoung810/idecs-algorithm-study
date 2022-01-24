import sys
input = sys.stdin.readline

def sup(M):
    m = len(M)
    result = True
    if m >1:
        itv = [i for i in range(m-1)]
        for i in itv:
            s = set()
            for j in range(m-1-i):
                _x = M[j]+M[j+1+i]
                s.add(_x)
            if len(s) != m-1-i:
                result = False
        return result
    else:
        return True
    
N = []
while True:
    a = input().rstrip()
    if a == '*':
        break
    N.append(a)
n = len(N)
for i in range(n):
    if sup(N[i]) == True:
        print(N[i], 'is surprising.')
    else:
        print(N[i], 'is NOT surprising.')