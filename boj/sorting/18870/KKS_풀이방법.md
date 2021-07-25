# boj 18870: 좌표 압축
> 문제 주소: https://www.acmicpc.net/problem/18870

### 1.문제설명
- 문제 설명  
    :리스트를 입력받으면 원소들이 몇번째로 작은 원소인지 바꿔서 출력해주면됨
    (이해하는데 좀 걸렸음..)
    
### 2.초기접근
- 중복된 원소 다 지우고 남은 고유의 원소들중에
- 내가 몇번째로 작은지 알면됨 (0~n)번째 까지

### 3.알아야하는 keyword
   a. enumerate
   b. set
   c. dictionary
   
### 4.접근 아이디어
# a. 일단 입력받음
# b. 입력받은 리스트를 set으로 캐스팅하고, 여기에 오름차순 정렬을 하고 다시 리스트로 바꿈
이때 원소들의 인덱스가 자신이 몇번째로 작은지 나타내는 것
# c.해시테이블 이용해서 딕셔너리에
원소 : 해당원소 인덱스 형식으로 저장해줌 그렇기위해 enumerate사용

### 5.코드구현
```python
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data2 = list(sorted(set(data)))
dic = {value : index for index, value in enumerate(data2)}

for item in data:
    print(dic[item], end = ' ')
```
