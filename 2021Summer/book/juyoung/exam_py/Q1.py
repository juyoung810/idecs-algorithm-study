# 그리디 유형 문제 -> '현재 상황에서 특정한 기준에 따라 가장 좋아 보이는 것만을 선택'
# 모험가 길드
# 공포도 X 이면 X 명 이상으로 그룹 구성 필요
# 공포도 높은 순으로 정렬해서, 그 공포도 만큼 사람 구성 --> 틀림
# 공포노 오름차순 정렬해서, 현재 그룹에 포함된 사람의 수가 현재 확인하고 있는 공포수 보다 같거나 크면, 그룹안에 들어올 수 있다.


import sys
input = sys.stdin.readline
# 사람 수 입력 받기
N = int(input())

# 공포도 입력 받기
fears = list(map(int,input().split()))

# 공포도 높은 순 정렬
fears.sort()

# 그룹 수 count
result = 0
# 현재 그룹안의 사람 수 count
count = 0

# 새로운 그룹마다 일단 그룹이라고 치고 넣고, 사람 수가 공포도 보다 크거나 같으면 그룹 결성하고, 새 그룹 형성하러
for i in fears:
    count += i # 현재 그룹에 해당 모험가 포함시키기
    if count >= i:
        result += 1
        count = 0



# 출력


print(result)
