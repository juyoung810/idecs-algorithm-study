import sys,collections
N = int(sys.stdin.readline())
array = []
# 수의 절댓값이 4000을 넘지 않으므로
counts = [0] * 8001
for _ in range(N):
    n = int(sys.stdin.readline())
    array.append(n)
    counts[n+4000] += 1  # 0 = 4000


# 산술 평균 출력
average = sum(array) / N
# 소수점 첫째 자리에서 반올림 -> round 함수 이용
sys.stdout.write(str(round(average))+"\n")

# 중앙값: N개의 수 증가 순 나열, 중앙값
array.sort()
max_num = array[N-1]
min_num = array[0]
sys.stdout.write(str(array[(N // 2)]) +"\n")

# 이미 counter 정렬되어있다.
count = collections.Counter(array)
count = count.most_common()
# dic = {arr: 0 for arr in set(array)}
# for arr in array:
#     dic[arr] += 1
#
# count = [[k, v] for k, v in dic.items()]
# count.sort(key = lambda x:x[0])
# count.sort(key = lambda x:x[1],reverse=True)
if len(count)>=2:
    if count[0][1] == count[1][1]: sys.stdout.write(str(count[1][0]) + "\n")
    else: sys.stdout.write(str(count[0][0]) + "\n")
else: sys.stdout.write(str(count[0][0]) + "\n")




# 범위 출력
sys.stdout.write(str(abs(max_num - min_num)))
