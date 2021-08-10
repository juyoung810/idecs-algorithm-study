'''
< 회의실 배정 >
각 회의에 대해 시작시간과 끝나는 시간이 있을 때, 각 회의 겹치지 않게 하면서 회의실 사용할 수 있는 회의의 최대 개수를 구하라!
시작시간이 빠른 것 부터 넣는게 유리. 시작시간이 같으면 빨리 끝나는 순서대로 정렬
'''

n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x:x[0]) # 시작시간으로 정렬
meeting.sort(key=lambda x:x[1]) # 끝나는 시간으로 정렬

end_time = 0
result = 0

for i, j in meeting:
    if i >= end_time:
        result += 1
        end_time = j

print(result)
