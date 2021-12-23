'''
1. input() 으로 입력 받으면 오류 -> sys.stdin.readline().strip()
2. 0 - len-1 index 돌면서 'X'일 경우 count +_1
    "." 일 경우 count % 4가 0일 경우 AAAA가 여러개 들어갈 수 있고, % 4 가 2일 경우
    AAAA가 몫 만큼, BB가 나머지의 /2의 몫 만큼 들어갈 수 있음을 의미

3. count % 4가 0또는 2가 아닐 경우 모두 들어갈 수 없으므로 -1

4. 마지막 경우 한번 더 확인

'''
import sys

board = sys.stdin.readline().strip()
ans = ""
count = 0

for i in range(len(board)):
    if board[i] != ".":
        count += 1
    else:
        if count % 4 == 2 or count % 4 == 0:
            ans += count//4 * ('AAAA') + (count % 4)//2 * ('BB')
            ans += "."
            count = 0
        else:
            ans = -1
            break


if count % 4 == 2 or count % 4 == 0:
        ans += count//4 * ('AAAA') + (count % 4)//2 * ('BB')
else:
    ans = -1

print(ans)


