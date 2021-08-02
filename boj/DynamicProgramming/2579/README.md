# boj 2579 : 계단오르기 by KKS
> 문제 주소: https://www.acmicpc.net/problem/2579
> 
> 난이도: silver 3

## 1.문제설명
- 계단을 오르는데 계단에 점수가 있음
- 계단은 한칸 또는 두칸씩 오를수있음
- 연속된 3개의 계단 밟으면 안됨
- 마지막 도착 계단은 무조건 밟아야됨
  (계단의 개수 300이하의 자연수)
## 2.문제해결 아이디어.
- 1차원 리스트의 그리드를 만들자
- 초기 세팅(?) 즉 점화식을 쓰기전에 앞으로 점화식에 쓰일 값들을 업데이트해줌
```python
cache[0] = score[0] #첫번째는 첫번째
cache[1] = (score[0]+score[1]) #두번째는 첫번째 + 두번째
#세번째 개단을 밟은 경우는 1칸,2칸 / 2칸,1칸 -> 이중에 최대
cache[2] = max(score[0]+score[2], score[1]+score[2]) #세번째
```
## 3.문제접근법
- 인덱스 3부터 n까지 반복

## 4.특별히 참고할 사항
- 문제 해결 아이디어 보면 계단의 갯수가 3개까지는 저렇게 설정했는데  
  사실 계단의 개수가 3개보다 적을수 있음 그래서 미리 score배열의 값을 모두 0으로 설정해야됨
- 아래 코드를 보고 이해할수 있음

## 5.코드구현
``` python
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
```