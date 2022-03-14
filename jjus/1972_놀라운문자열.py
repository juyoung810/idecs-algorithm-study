"""
구현
- 모든 조건 확인할 수 있도록 이중 for문 -> O(N^2)
- set 통해 중복된 것 있는 지 확인

68ms
"""
import sys

input = sys.stdin.readline


def checkAmazing():
    D = []
    for i in range(1, len(arr) - 2 + 1):
        for j in range(len(arr) - 1 - i + 1):
            D.append(arr[j] + arr[j + i])
        if len(D) != len(set(D)):
            return False
        else:
            D = []
    return True


arr = input().rstrip()
while arr != "*":
    if checkAmazing():
        print(arr + " is surprising.")
    else:
        print(arr + " is NOT surprising.")
    arr = input().rstrip()
