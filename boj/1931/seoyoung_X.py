### 회의실 배정
## 한 개의 회의실. 사용하고자 하는 n개의 회의. 회의실 사용표 만들기!
## 각 회의에 대해 시작시간과 끝나는 시간 있음. 각 회의 겹치지 않게 하면서 회의실 사용할 수 있는 회의의 최대 개수

n = int(input())   # 회의의 수
meeting = []
cnt = 0

for i in range(n):
    info = list(map(int, input().split()))
    meeting.append(info)

