import sys
input = sys.stdin.readline
N = int(input())
data = []
for _ in range(N):
    name, kor, eng, math = input().split()
    data.append((name, int(kor), int(eng), int(math)))
'''
data.sort(key=lambda x: x[0])
data.sort(key = lambda x:x[3], reverse = True)
data.sort(key = lambda x:x[2])
data.sort(key= lambda x:x[1], reverse= True)
'''
data.sort(key = lambda x : (-x[1] , x[2],-x[3],x[0]) )
for i in data:
    print(i[0])