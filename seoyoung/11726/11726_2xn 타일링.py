'''
2Xn 크기의 직사각형을 1X2, 2X1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 n
출력 : 첫째 줄에 2Xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력

'''

import sys

n = int(input())
d = [1,2,3]

if n <= 3:
    print(d[n-1])
    sys.exit(0)

for i in range(3,n):
    d.append(d[i-1]+d[i-2])

print(d[-1]%10007)