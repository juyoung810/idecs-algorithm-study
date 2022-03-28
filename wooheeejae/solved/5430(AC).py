case = int(input())

for i in range(case):
    funList = list(input())
    cntR = 0 # R의 갯수 확인
    N = int(input())
    numList = input()

    if N == 0: # 안에 있는게 없으면 바로 []로 리턴
        numList = []
    elif N == 1: # 안에 있는게 하나일 경우
        numList = [numList[1:-1]]
    else:
        numList = list(map(int, numList[1:-1].split(',')))

    # 지우는 갯수가 입력한 숫자 갯수보다 클 경우
    if funList.count('D') > len(numList):
        print('error')
        continue

    for j in funList:
        if len(numList) == 0:
            break
        if j == 'R':
            if cntR == 0: # 0 혹은 짝수 일 때
                cntR = 1
            else: # 홀수개
                cntR = 0
        elif j == 'D':
            if cntR == 0: # 0 혹은 짝수 일 때
                del numList[0]
            else:
                del numList[-1]
    if len(numList) == 0:
        print('[]')
    else:
        if cntR == 0:  # 0 혹은 짝수 일 때
            print('[' + ','.join(map(str, numList)) + ']')
        else:
            numList.reverse()
            print('[' + ','.join(map(str, numList)) + ']')
