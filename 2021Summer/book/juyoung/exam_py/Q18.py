## 올바른 문자열인지 확인하는 함수
# 0 - 끝 같은지 확인 하고 같으면 삭제
# 하나라도 다른 경우 올바른 문자열이 아니다.
def check_correct(p):
    p = list(p)
    while p:
        if p[0] == "(" and p[len(p)-1] == ")":
            p.remove(p[0])
            p.remove(p[len(p) - 1])
        else:
            return False
    return True


# 문자열 균형 잡힌  u와 나머지 v로 나누기
def half_String(p):
    x = 0  # ( 의 갯수
    y = 0  # ) 의 갯수
    p1 = ""
    p2 = ""
    for i in range(len(p)):
        if p[i] == "(":
            x += 1

        else:
            y += 1
        p1 += p[i]

        if x == y:
            if i+1 != len(p):
                p2 += p[i+1:]
            break
    return p1, p2


def solution(p):
    answer = ''
    # 문자열 두개로 나누기
    u, v = half_String(p)
    if check_correct(u):
        answer += u
        if v != "":
            answer += solution(v)
    else:
        answer += "("
        if v != "":
            answer += solution(v)
        answer += ")"
        for i in range(1, len(u) - 1):
            if u[i] == "(":
                answer += ")"
            else:
                answer += "("

    return answer


print(solution(str(input())))
