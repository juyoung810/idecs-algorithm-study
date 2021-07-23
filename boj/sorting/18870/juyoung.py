# 입력 받은 좌표를 각각 자기 자신 보다 작은 값을 counting 한 갯수의 값으로 변경해서 출력하기
# 배열을 입력 받은 다음, 오름 차순으로 정렬한 후 자기 자신이 나오기 전까지의 갯수를 count 한다.
import sys
N = int(sys.stdin.readline())

array = list(map(int,sys.stdin.readline().split()))
# [index,value] 리스트 만들기
array = [[i,array[i]] for i in range(N)]
# value를 오름 차순으로 정렬한다.
array.sort(key = lambda x:x[1])

# 각 index 별 자기 자신 보다 작은 value 찾기 위한 list 만든다.
count = [[0,0] for _ in range(N)]

# 가장 작은 value의 index 저장
count[0][0] = array[0][0]
for i in range(1,N):
    # index 저장
    count[i][0] = array[i][0]
    # 정렬된 value 가 중복 되지 않을 경우 이전의 count + 1
    if array[i-1][1] != array[i][1]:
        count[i][1] = count[i-1][1] + 1
    # 이전거랑 같은 경우 이전 count랑 같다.
    else: count[i][1] = count[i-1][1]

# count 배열을 다시 index 순으로 정렬
count.sort(key = lambda x: x[0])

for i in range(N):
    sys.stdout.write(str(count[i][1]) + " ")











