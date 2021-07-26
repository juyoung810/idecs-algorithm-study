# 떡볶이 떡 만들기
# 절반기 높이 H 정해서 -> 떡을 절단기로 자르고 난 후 잘린 값을 다 더해서 고객이 가져간다.
# 고객 요청 M 일 때 적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기

# 최대 주어진 떡의 길이보다 작거나 같아야 한다. -> H : 0 ~ max(떡의 길이)


N,M = map(int,input().split())
r_list = list(map(int,input().split()))

# 이진 탐색 위한 시작점과 끝점
start = 0
end = max(r_list)

# 현재 얻을 수 있는 떡볶이 양에 따라 자를 위치 결정 -> 반복적으로 돌리는게 적절하다
result = 0
while (start <= end):
    total = 0
    mid = (start + end)//2
    for x in r_list:
        if x > mid:
            total += x-mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < M:
        end = mid -1
    # 떡의 양이 충분한 경우 덜 자르게 하기 위해 오른쪽 부분을 탐색한다.
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 , result 기록한다.
        start = mid +1


print(result)