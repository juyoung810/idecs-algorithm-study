import sys
input = sys.stdin.readline

N = int(input())

# 새로 추가된 문자 + 앞의 문자열 같은지 확인
def b_same(str,i):
    t_str = str[:]
    t_str.append(i)
    n = len(t_str)
    for i in range(1,n//2+1):
        if t_str[-i:] == t_str[-2*i :-i]:
            return True
    return False


# 백트래킹
def dfs(N,current,candidate):
    if current == N:
        result_str = ''.join(str(x) for x in candidate)
        print(result_str)
        exit()
    for i in range(1,4):
        if not b_same(candidate,i):
            candidate.append(i)
            dfs(N,current+1,candidate)
            candidate.pop()

result = []
dfs(N,0,result)