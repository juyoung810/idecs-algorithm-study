'''
## 실패율
> 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42889

### 문제
- 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
- 전체 스테이지의 개수 n, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어진다
- 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열을 return 하도록 solution 함수를 완성하라!

### 제한사항
- stages에는 1 이상 n+1 이하의 자연수가 담겨있다.
    - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다
    - n+1은 마지막 스테이지까지 클리어한 사용자를 나타낸다
- 만약 실패율 같은 스테이지 있으면 작은 번호의 스테이지가 먼저 오도록
- 스테이지에 도달한 유저 없는 경우 해당 스테이지 실패율은 0

### 문제 해결 방향
- 각 스테이지에 대해서, 머물러있는 사람의 수를 저장한다.
- 거꾸로 더하면 각 스테이지에 도달한 사람의 수를 계산할 수 있다.
- 거꾸로 더하지 않는 방법 : 전체 플레이어의 수에서 현재 칸에 머물러 있는 사람을 제외하면 다음 스테이지에 도달한 사람이다.
- 실패율은 도달한 사람을 머물러있느 사람으로 나눈 수이다.
'''

n = int(input())
stages = list(map(int, input().split()))

def solution(N, stages):
    p_stay = [0 for _ in range(N+2)]
    p_arrive = [0 for _ in range(N+2)]
    fail = []
    for i in range(1, N+2):
        p_stay[i] = stages.count(i)
    p_stay_r = reversed(p_stay)
    for i in range(1, N+1):
        p_arrive[i] = p_arrive[i-1] + p_stay_r[i]
    for i in range(1, N+1):
        fail.append([i, p_stay[i] / p_arrive[i]])

    answer = sorted(fail, key = lambda x: x[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer


def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        stay = stages.count(i)

        if stay == 0:
            failure = 0
        else:
            failure = stay / length

        answer.append([i, failure])
        length -= stay

    answer = sorted(answer, key=lambda x: x[1], reverse=True)

    answer = [i[0] for i in answer]

    return answer