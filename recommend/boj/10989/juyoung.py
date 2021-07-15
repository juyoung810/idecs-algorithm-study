import sys
N = int(sys.stdin.readline())
lst = [0] * 10001

for _ in range(N):
    lst[int(sys.stdin.readline())] += 1

for i in range(1,10001):
    for _ in range(lst[i]):
        sys.stdout.write(str(i)+'\n')

# def find_index(lst,n,size):
#     # 비어있는 리스트일 경우 index 0에 삽입
#     if size == 0:
#         return 0
#     min = lst[0]
#     max = lst[size-1]
#     if n >= max:
#         return size
#     elif n <= min:
#         return 0
#     else:
#         for i in range(1,size):
#             # n이 lst의 요소 보다 작거나 같은 index 찾는다.
#             if n <= lst[i]:
#                 return i
#
# size = 0
# for i in range(N):
#     n = int(input())
#     lst.insert(find_index(lst,n),n,size)
#     size += 1
#     #print(lst)
#
#
# for i in range(N):
#     print(lst[i])