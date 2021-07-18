### 시각
## 정수 n이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

n = int(input())
cnt = 0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            time = str(hour) + str(minute) + str(second)
            if '3' in time:
                cnt += 1

print(cnt)