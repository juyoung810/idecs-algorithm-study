'''
8시가 될때까지 문앞에 줄 세워놓고, 8시 되는 순간 손님들은 모두 입구에서 커피를 하나씩 받고 자리로 간다.
손님들이 입구에 들어갈 때, 강호에게 팁을 준다. 손님들은 자기가 커피를 몇 번째 받는지에 따라 팁을 다른 액수로 강호에게 준다.
원래 주려고 생각했던 돈 - (받은 등수 -1) 만큼의 팁을 준다. 음수라면, 팁을 받을 수 없다.
스타벅스 앞에 있는 사람의 수 N과, 각 사람이 주려고 생각하는 팁이 주어질 때, 손님의 순서를 바꿔 받을 수 있는 팁의 최댓값은?

입력 : 첫째줄은 스타벅스 앞에 서 있는 사람의 수 N, 둘째줄부터 총 N개의 줄에 각 사람이 주려고 하는 팁
출력 : 받을 수 있는 팁의 최댓값

< 아이디어 >
1. 내림차순으로 정렬해서, 앞에 있던 사람 수만큼 뺀다.(인덱스만큼 뺀다)
'''

n = int(input())
line = []
idx = 0
result = 0

for _ in range(n):
    line.append(int(input()))
line.sort(reverse=True)

for tip in line:
    tip -= idx
    if tip < 0:
        continue
    result += tip
    idx += 1

print(result)


# 답지
n = int(input())
a = []
s = 0

for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)

for i in range(n):
    b = a[i] - i

    if b > 0:
        s += b

print(s)
