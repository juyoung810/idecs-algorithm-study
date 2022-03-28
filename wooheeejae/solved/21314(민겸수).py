import sys
input = sys.stdin.readline

mkNum = input()
tempStr = ''
cnt = 0

# 최댓값출력
for i in range(len(mkNum)):
    # M을 만나면 카운트를 하나씩 셈
    if mkNum[i] == 'M':
        cnt += 1
        # 마지막에 M이 나오는 경우
        if i == len(mkNum) - 2:
            tempStr += (str(1) * cnt)
            break
    # K를 만나면 카운트 수만큼 10의 거듭제곱에 5를 곱한 수 를 더함
    # 카운트를 소모함.
    elif mkNum[i] == 'K':
        if cnt == 0:
            tempStr += str(5)
        elif cnt >= 1:
            tempStr += str(5 * (10**cnt))
            cnt = 0
print(int(tempStr))
tempStr = ''
cnt = 0

# 최솟값 출력
for i in range(len(mkNum)):
    # M을 만나면 카운트를 하나씩 셈
    if mkNum[i] == 'M':
        cnt += 1
        # 마지막에 M이 나오는 경우
        if i == len(mkNum) - 2:
            tempStr += (str(10**(cnt-1)))
            break
    # K를 만나면 카운트만큼 10의 거듭제곱을 더하고 K를 만났으므로 1의 자리에 5를 더함.
    # 카운트를 소모함
    elif mkNum[i] == 'K':
        if cnt == 0:
            tempStr += str(5)
        elif cnt >= 1:
            tempStr += str(10 ** cnt + 5)
            cnt = 0
print(int(tempStr))