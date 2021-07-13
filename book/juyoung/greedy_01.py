N,M,K = map(int,input().split())

data = list(map(int,input().split()))

# 주어진 수 정렬하기 (내림차순)
data.sort()

num1 = data[N-1]
num2 = data[N-2]



# 가장 큰 수 * K * (M//K) + 두번째로 큰 수 * (M%K)

# big_num = num1 * K * (M//K) + num2 *(M%K)


## 반복되는 수열의 방법 이용
# 반복되는 수열의 길이 : K+1
# 반복되는 수열 횟수 : M // (K+1)
# 나누어 떨어지지 않는 경우 -> 나머지 만큼 가장 큰 수 더한다. 가장큰수*(M%(K+1)

# big_num = (num1*K+num2) * (M//(K+1)) + (num1 * (M% (K+1)))

# 가장 큰 수가 더해지는 횟수
count =( M // (K+1) )* K + M % (K+1)

big_num = count * num1
big_num += num2 * (M-count)
print(big_num)