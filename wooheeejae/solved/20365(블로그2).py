 # 기본 변수 설정
N = int(input())
col = list(input())
cnt = 0

 # 문제 풀이
# 색이 바뀌는 구간 갯수
for i in range(N-1):
     if col[i] != col[i+1]:
         cnt += 1

# 처음과 끝이 같을 때
if col[0] == col[-1]:
    print(int(cnt/2 + 1))
# 처음과 끝이 다를 떄
else:
    print(int((cnt+3)/2))
