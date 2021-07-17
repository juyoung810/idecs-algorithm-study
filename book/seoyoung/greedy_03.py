### 1이 될 때까지
## 어떠한 수 n이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택해 수행
## 단, 두 번째 연산은 n이 k로 나누어떨어질 때만 선택가능
## 1. N에서 1을 뺀다.
## 2. N을 K로 나눈다.
## N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램 작성

# 입력 조건 : 첫째 줄에 N과 K가 공백으로 구분되며 각각 자연수로 주어진다. 이때 N >= K

# n , k = map(int, input().split())

# result = n
# cnt = 0
#
# while result != 1:
#     if result % k == 0:
#         result /= k
#         cnt += 1
#     if result % k != 0:
#         result -= 1
#         cnt += 1

# print(cnt)

# 계속 돌아가나... 쨋든 틀린듯..ㅋ

# 그리디를 생각하자..! 계속 나눌 수 있는게 아니니까 나눌 수 있을 때까지 나누기. 나누고 빼지 못할 때 까지의 횟수
# 다 나누고 나서는 1 될때까지 빼기. 남은 수에서 1 뺀 수

n, k = map(int, input().split())
cnt = 0

while True:
    if n < k:
        break
    if n % k != 0:
        n -= 1
        cnt += 1
    n /= k
    cnt += 1

cnt += n-1

print(cnt)