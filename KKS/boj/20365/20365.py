import sys
input = sys.stdin.readline

N = int(input())
tasks = input().rstrip()
color_dict = {'B' : 0, 'R' : 0}
color_dict[tasks[0]] += 1
for i in range(1, N):
    if tasks[i] != tasks[i-1]:
        color_dict[tasks[i]] += 1
print(min(color_dict['R'], color_dict['B']) + 1)

