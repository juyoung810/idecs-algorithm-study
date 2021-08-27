'''
< 모험가 길드 >
N명의 모험가를 대상으로 공포도 측정. 공포도 높으면 위험 상황에서 제대로 대처 못함.
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다.
최대 몇 개의 모험가 그룹을 만들 수 있나?
공포도가 작은 모험가끼리 먼저 묶는다!
'''

n = int(input())
fear = list(map(int, input().split()))

fear.sort()

count = 0   # 인원수 셀 변수
result = 0  # 그룹 수 셀 변수

for i in fear:
    count += 1  # 그룹에 인원을 추가한다.
    if count == i:  # 그룹 인원 수와 공포도가 일치하면
        result += 1 # 그룹으로 묶는다.
        count = 0   # 인원수를 초기화한다.

print(result)