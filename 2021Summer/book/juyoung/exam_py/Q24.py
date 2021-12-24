# 특정 위치의 집에 특별히 한 개의 안테나 설치
# 안테나로부터 모든 집까지의 거리 총합 최소
# 안테나는 집이 위치한 곳에만 설치 가능
# 동일한 위치에 여러개의 집 존재 가능
# 안테나 설치 위치 값이 여러개 도출될 겨우 가장 작은 값 출력


import sys

input = sys.stdin.readline
n = int(input())

# 집위치 입력 받기
arr = list(map(int, input().split()))
# dp = [[arr[i],0] for i in range(len(arr))]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         dp[i][1] += abs(arr[i]-arr[j])
#         dp[j][1] += abs(arr[i]-arr[j])
#
#
# dp.sort(key=lambda x:(x[1],x[0]))
# # 거리 작은 순 정렬 -> 여러 값 도출 경우 작은 값
# print(dp[0][0])
arr.sort()
print(arr[(n-1)//2])


