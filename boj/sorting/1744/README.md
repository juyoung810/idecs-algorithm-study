# boj 1744: 수 묶기 by KKS
> 문제 주소: https://www.acmicpc.net/problem/1744

### 1.문제설명
- -10000~10000사이의 숫자가 담긴 리스트가 주어짐
- 리스트에 있는 숫자끼리 묶어서 최대의 값을 구하면됨  
    ex) [0, 1, 2, 4, 3, 5] 를 그냥 더하면 15인데  
    잘 묶으면  0+1+(2*3)+(4*5) = 27 이렇게됨
- 문재를 잘 이해해야됨 붙어있지 않아도 묶을수 있음

### 2.초기접근
- 리스트에 있는 수를 내림차순으로 sort해서
- 붙어있는 수가 양수라면 묶어주고 음수는 그냥 더하고 음수끼리는 묶어서 곱해주려함

### 3.간과한 사실
- 바보같지만 서로 붙어있는거끼리만 묶을수 있는 줄 알았음...
- 1은 곱하는거보다 더하는게 더 커짐

### 4.케이스 구분
1. 양수, 양수 = 곱
2. 양수, 0 = 묶으면 안됨
3. 음수, 음수 = 곱
4. 음수, 0 = 곱 
5. 1은 무조건 그냥 더해야됨

### 5. 새로운 전략
- 입력받을때 양수는 양수끼리, 음수는 음수끼리 모으자
- 1은 결과를 maxmize하기 위해서는 모으지않고 1을 더해버리면 됨
- 0은 곱해도 음수랑 곱하자

### 6. 코드구현
## a. 입력받기 위한 준비 
``` python
import sys
input = sys.stdin.readline
n = int(input())
positive = []
negative = []
result = 0
```
## b. 입력받기
``` python
for _ in range(n):
    value = int(input())

    if value>1:
        positive.append(value)
    elif value == 1: #처음에 여기서 실수 1은 곱하는거보단 더하는게 더 커짐
        result += 1
    else:
        negative.append(value)
```
## c. 정렬
``` python
positive.sort(reverse=True) #큰수부터-> 양수는 큰수부터 곱
negative.sort() #작은수부터 -> 음수는 작은 수일수록 절대값이 크니깐 작은수부터 곱
```

## d. 더해보자 
``` python
if len(positive) % 2 == 0: #길이가 짝수면 2스텝씩 증가하면서 아래를 진행하면됨
    for i in range(0, len(positive), 2):
        result += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive)-1, 2): # 끝 -1까지 간다음 마지막 원소는 그냥 더해주면됨
        result += positive[i] * positive[i + 1]
    result += positive[len(positive)-1]
#위와 동일
if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        result += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        result += negative[i] * negative[i + 1]
    result += negative[len(negative)-1]

print(result)

```
