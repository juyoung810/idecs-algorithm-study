n = int(input())
score = [0] * 300
for i in range(n):
    score[i] = int(input())

cache = [0] * 300
cache[0] = score[0] #첫번째는 첫번째
cache[1] = (score[0]+score[1]) #두번째는 첫번째 + 두번째
cache[2] = max(score[0]+score[2], score[1]+score[2]) #세번째
for i in range(3,n):
    cache[i] = max(cache[i-2]+score[i],cache[i-3] +score[i-1] + score[i]) #두칸 점프해서 현재 칸을 밟은 경우, 한칸 한칸해서 밟은 경우우
print(cache[n-1])