def divide(p):
    start, close = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            start += 1
        else:
            close += 1
        if start == close:
            return p[:i + 1], p[i + 1:]

def isbalanced(u):
    stack = []
    for s in u:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    answer = ''
    #조건1
    if not p:
        return answer
    # 균형잡힌  -> ( )갯수가 맞는 case
    # 옳바른 -> () 군형잡혔으면서 짝이 맞는경우
    u, v = divide(p)
    if isbalanced(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

    return answer