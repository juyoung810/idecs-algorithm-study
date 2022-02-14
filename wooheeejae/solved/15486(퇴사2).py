import sys
input = sys.stdin.readline

 # 기본 변수 설정
days = int(input())
TP = [list(map(int,input().split())) for i in range(days)]
temp = [0] * (days+2)
 # 문제풀이
for i in range(days):
    # TP[i][0] : 일하는데 걸리는 날짜
    # days - i : 남은 날
    if TP[i][0] <= days - i:
        # temp[i+TP[i][0]] : i번째 날 + i번째 날 일이 끝나는 다음날
        # i번째 날이 되었을때
        #  temp[i+TP[i][0]] : 오늘 일 안했을 때 오늘 일이 끝나는 날 받을 돈
        #  temp[i] + TP[i][1] : 어제까지 일한 돈과 오늘일까지 하고 받을 돈
        temp[i+TP[i][0]] = max(temp[i+TP[i][0]], temp[i] + TP[i][1])
    # temp[i+1] : i번째 날까지 일하고 번 최대 돈
    temp[i+1] = max(temp[i+1], temp[i])

print(max(temp))