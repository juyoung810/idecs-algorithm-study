"""
구현
1. 공백 문자 모두 제거 -> split()
2. list의 원소 수로 띄어쓰기 갯수 확인
3. title 생성 후 list에 append
4. 각 word가 알파벳 갯수가 남았고 이전 문자와 다를 경우 알파벳 수 -1
--> set 사용할려고 했는데 그렇게 하면 연속되지 않는 문자도 없어져버리므로 틀림

76ms
"""
import sys

input = sys.stdin.readline


# 띄어쓰기 기준 먼저 확인
def check_arr():


    if N < len(arr) - 1:
        return -1

    #타이틀 생성
    title = ""
    for word in arr:
        title += word[0].upper()
    arr.append(title)

    for word in arr:
        pre = ""
        for one in word:
            if alpha[ord(one.upper()) - 65] != 0:
                if pre != one:
                    alpha[ord(one.upper()) - 65] -= 1
                    pre = one
                else:
                    continue
            else:
                return -1
    return title


arr = input().rstrip().split()
N = int(input())
alpha = list(map(int, input().rstrip().split()))
print(check_arr())
