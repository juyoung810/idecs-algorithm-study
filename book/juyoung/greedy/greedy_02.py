N,M = map(int,input().split())

# # dictionary key : index, value = list로 설정
# r_lst = {}
# for i in range(N):
#     r_lst[i] = list(map(int,input().split()))
# # 각 행을 오름차순 정렬
#     r_lst[i].sort()
#
# # 0 번째 index가 가장 큰 row의 0 번째 index 선택
# max = r_lst[0][0]
# for j in range(1,N):
#     if max < r_lst[j][0]: max = r_lst[j][0]


## python은 min, max 함수가 존재한다!
max_num = 0
for i in range(N):
    data = list(map(int,input().split()))
    max_num = max(min(data),max_num)

print(max_num)