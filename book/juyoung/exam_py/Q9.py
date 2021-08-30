# 문자열 주어진 문제 그대로 처리할 수 있도록 한다.
def solution(s):
    # 문자열의 길이 저장
    length = len(s)

    # 최대로 긴 길이 = 문자열 그 자체의 길이
    answer = length
    # step (단위) = 1 ~ length //2
    for step in range(1,length//2 +1):
        # 결과 문자 열 저장
        result = ""
        # 비교하는 이전 문자열 저장
        temp = s[0:step]
        # 똑같은 것을 count = 1 부터 시작
        count = 1
        # 0-2 VS 2*1-2*2 VS 2*2-2*3 ... 2 * (길이/단위 -1)- 2*(길이/단위)
        for i in range(1,length//step):
            if temp == s[step*i:step*(i+1)]:
                count += 1
            else:
                if count >= 2:
                    result += str(count) + temp
                    count = 1
                else:
                    result += temp
                temp = s[step * i:step * (i + 1)]
        # 끝까지 남은 것 계산 위해
        if count >= 2:
            result += str(count) + temp
        else:
            result += temp
        # 단위에 포함되지 않은 것 그대로 더한다.
        if length % step != 0:
            result += s[step *(length//step):length]
        # 결과의 길이 제일 작은게 답
        answer = min(answer,len(result))
    return answer

s = input()
print(solution(s))