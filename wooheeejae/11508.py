#2+1세일
 # 기본 변수 설정
milkNum = int(input())
milkPrice = []
answer = 0

for i in range(milkNum):
    milkPrice.append(int(input()))

 # 문제 풀이
milkPrice.sort(reverse=True)

for i in range(milkNum // 3):
    milkPrice[(i+1)*3-1] = 0

for j in range(milkNum):
    answer += milkPrice[j]

print(answer)
