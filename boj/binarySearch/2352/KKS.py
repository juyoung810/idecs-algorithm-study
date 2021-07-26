import sys
input = sys.stdin.readline
n = int(input())
connection = list(map(int,input().split()))
lis = []

def lowerbound(lis,x):
    start, end = 0, len(lis)-1

    while start <= end:
        mid = (start+end)//2
        if lis[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

for x in connection:
    if not lis or lis[-1] < x:
        lis.append(x)
    else:
        lis[lowerbound(lis,x)] = x

print(len(lis))