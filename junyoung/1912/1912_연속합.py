import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr_sum = [0] * n
arr_sum[0] = arr[0]
for i in range(1, n):
    if arr_sum[i-1] > 0 :
        arr_sum[i] = arr_sum[i-1]+arr[i]
    else:
        arr_sum[i] = arr[i]
        
print(max(arr_sum))

##############################################'
# 4가지 경우로 나누어 생각하면 위와 동일한 결과이므로 묶어서 생각하면 됨
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# arr_sum = [0] * n
# arr_sum[0] = arr[0]
# for i in range(1, n):
#     if arr_sum[i-1] >0 and arr[i] >0 : 
#         arr_sum[i] = arr_sum[i-1] + arr[i]
#     elif arr_sum[i-1] >0 and arr[i] <0 :
#         arr_sum[i] = arr_sum[i-1] + arr[i]
#     elif arr_sum[i-1] <0 and arr[i] >0 :
#         arr_sum[i] =  arr[i]
#     else
#         arr_sum[i] = arr[i]
        
# print(max(arr_sum))