### 큰 수의 법칙

# n, m, k를 공백 구분해 입력받기
n, m, k = map(int, input().split())

# n개의 수를 공백 구분해 입력받기
data = list(map(int, input().split()))

# 배열 정렬
data.sort()
print(data)

first = data[-1]
second = data[-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)


# 이렇게 하면 쉬운 방법... 반복되는 수열에 대해서 파악하기
# 큰 수가 k번 더해진 후 그 다음 수가 1번 반복된다. k * first + second 가 m을 (k+1)로 나눈 몫만큼 반복, 나머지만큼 first 반복

n, m, k = map(int, input().split())   # n, m, k를 공백으로 구분해 입력받기
data = list(map(int, input().split()))   # 배열 공백으로 구분해 리스트로 입력받기

data.sort()   # 입력받은 숫자 정렬
first = data[-1]   # 가장 큰 수
second = data[-2]   # 두번째로 큰 수

# 가장 큰 수 k번 더하고 두번째 수 한번 더하는거 반복할 횟수 계산
cnt = m // (k + 1)
last = m % (k + 1)

# 결과 계산
result = 0
result += cnt * (k * first + second)
result += last * first

print(result)