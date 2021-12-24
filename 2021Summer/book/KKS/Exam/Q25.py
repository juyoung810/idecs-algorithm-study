def solution(N, stages):
    #N: 스테이지의 갯수, stages:현재 도전중인 stage
    #stage : 실패율 = 스테이지 도달 클리어 x/스테이지 도달
    #stage 원소의 뜻은 현재 원소에 도전중 클리어 X
    length = len(stages)
    failure_rate = []
    stages.sort()
    for i in range(1,N+1):
        if i not in stages:
            failure_rate.append((i,0))
        else:
            failure_rate.append((i, stages.count(i)/(length - stages.index(i))))
    failure_rate.sort(key = lambda x:(-x[1], x[0]))

    answer = []
    for stage in failure_rate:
        answer.append(stage[0])
    return answer

print(solution(4,	[4,4,4,4,4]))