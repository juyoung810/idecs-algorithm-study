# 가장 긴 증가하는 수열
import sys

N = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))


# up_list = []
# 각각의 원소 마다 증가하는 부분 수열의 길이 저장하기   -> O(N^2) 걸린다.
# for i in range(N):
#     length = []
#     for j in range(i,N):
#         if array[j] < array[i]:
#             break
#         elif array[j] > array[i] and array[j] not in length:
#             length.append(array[j])
#
#     up_list.append(len(length)+1)
# sys.stdout.write(str(max(up_list)))
#

def binarySearch(lis,target):
    start = 0
    end = len(lis)-1
    while start <= end:
        mid = (start + end) //2
        if lis[mid] == target:
            return mid
        elif lis[mid] > target:
            end = mid -1
        else: start = mid +1

    return start

# lis = []
# for arr in array:
#     if not lis:
#         lis.append(arr)
#     else:
#         idx = binarySearch(lis,arr)
#         if idx >= len(lis):
#              lis.append(arr)
#         else:
#             lis[idx] = arr
#
# print(len(lis))
# # 이분 탐색 통해 lis 구하기
lis = []
lis.append(array[0])
length = 1
for i in range(1, N):
    if array[i] > lis[length]:
        # lis 에 들어있는 가장 마지막 값보다 큰 경우, 바로 맨 뒤에 넣는다.
        lis.append(array[i])
        length+=1
    # lis에 들어갈 수 있는 해당 원소의 위치를 찾는다. -> 이분탐색
    else:
        lis[binarySearch(lis,array[i])] = array[i]

print(lis)
sys.stdout.write(str(length))


