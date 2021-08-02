#왼쪽부터 턴다고 가정
# i 번째에서 터는 여부를 결정할때, 나 + 나 -2 를 한 결과 vs 나 -1 를 털었을 때 결과 더해서 뭐가 더 큰지 결정한다

n = int(input())
array = list(map(int,input().split()))

# dp table
d = [0] * 100
# 0 번째 턴 경우
d[0] = array[0]
# 1번 털 경우 -> 0 번 터는 것 보다 1 번 터는게 더 클경우
d[1] = max(d[0], array[1])

# i = 2번부터 n-1 까지 비겨
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2] + array[i]) # i-1 번까지 잘 더한거랑 d-2 + 내거 했을 떄 더 크면 그 값을 바꾼다.

print(d[n-1])