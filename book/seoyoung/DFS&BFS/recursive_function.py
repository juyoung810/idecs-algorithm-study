# 재귀함수의 종료 조건

def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

# 컴퓨터 내부에서 재귀함수의 수행은 스택 자료구조를 이용

## 두가지 방식으로 구현한 팩토리얼 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_reculsive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)! 을 그대로 코드에 적용하기
    return n * factorial_reculsive(n-1)

print('반복적 구현 : ', factorial_iterative(5))
print('재귀적 구현 : ', factorial_reculsive(5))
