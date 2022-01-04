'''
정수 4를 1,2,3의 합으로 나타내는 방법은 총 7가지. 합을 나타낼 때는 수를 1개 이상 사용해야함.
정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 구하는 프로그래을 작성하자.

< 아이디어 >
1. 점화식을 찾는다
2. 값을 새로 구해 더한다.

근데 11보다 작다고 했으니까 10까지면 그냥 10까지 구해서 출력해도 될것같은데?
-> 이러면 코드는 줄어드는데 시간이 길어짐
'''

# 테스트 케이스 입력받기
T = int(input())

for _ in range(T):
    n = int(input())
    d = [1,2,4]
    for i in range(3,n):
        d.append(d[i-1]+d[i-2]+d[i-3])
    print(d[n-1])



# 새로운 버전
T = int(input())
d = [0,1,2,4]
result = []

for i in range(4,11):
    d.append(d[i-1]+d[i-2]+d[i-3])

for _ in range(T):
    n = int(input())
    print(d[n])