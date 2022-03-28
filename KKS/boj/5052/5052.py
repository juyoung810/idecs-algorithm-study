import sys
input = sys.stdin.readline
t = int(input())
def solve():
    n = int(input())
    phone_list = []
    for i in range(n):
        phone_list.append(input().rstrip())
    phone_list.sort()
    for i in range(len(phone_list)-1):
        if phone_list[i] in phone_list[i+1][:len(phone_list[i])]:
            return print("NO")
    return print("YES")

for _ in range(t):
    solve()