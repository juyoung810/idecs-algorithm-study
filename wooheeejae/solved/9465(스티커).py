 # 기본 변수 설정
rep = int(input())
answer = [0 for i in range(rep)]
 # 문제풀이
for i in range(rep):
    n = int(input())
    sti = [list(map(int, input().split())) for m in range(2)] # 스티커 2차원배열 구성
    # 한 줄일 때는 위 아래 비교 후 큰 것 출력
    if n == 1:
        answer[i] = max(sti[0][0], sti[1][0])
    # sti[0][1]과 sti[1][1]은 2번째 전 인덱스가 없으므로 미리 설정
    else:
        sti[0][1] += sti[1][0]
        sti[1][1] += sti[0][0]
        # [][2]부터 시작해서 대각선 반대쪽 전 과 전전 자리와 비교하여 큰값과 더함
        for j in range(2, n):
            sti[0][j] += max(sti[1][j - 1], sti[1][j - 2])
            sti[1][j] += max(sti[0][j - 1], sti[0][j - 2])
        answer[i] = max(sti[0][n - 1], sti[1][n - 1])

for k in answer:
    print(k)