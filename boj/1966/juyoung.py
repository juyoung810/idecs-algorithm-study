# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    priority = list(map(int,input().split()))
    paper = []
    count = 0
    # 큐 만들기
    for i in range(N):
        paper.append((i,priority[i]))

    while True:
        max_priority = max(paper, key= lambda x:x[1])
        if paper[0][1] >= max_priority[1]:
            if paper.pop(0)[0] == M:
                count+=1
                print(count)
                break
            else: count+=1
        else:
            paper.append(paper.pop(0))