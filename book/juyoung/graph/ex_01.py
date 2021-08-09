# 팀 결성
# 0 ~ N 까지의 노드 존재
# 0 a b 에 대해서 a ,b union 연산 실행
# 1 a b에 대해 a,b 두 연산이 같은 집합인지 확인 하는 연산 실행

# n : 학생의 번호 0~N, m: 연산 횟수
n, m = map(int, input().split())

# 부모 노드 저장 위해 n+1 리스트 생성
parent = [0] * (n + 1)

# 부모 노드를 자기 자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i


# 부모를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:  # 자신이 루트 노드가 아닐 경우
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union 연산 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 연산 입력 받기 0 : 합 연산, 1: 확인 연산
for _ in range(m):
    what, a, b = map(int, input().split())
    if what == 0:
        union_parent(parent, a, b)
    elif what == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")
