# <span style="color:blue">boj 2108: 통계학</span>
> 문제 주소: https://www.acmicpc.net/problem/2108
> 
> silver 4


# 문제 해결 방법
- 반올림 : round() 함수 사용
- 절댓값: abs() 함수 사용

- 최빈 값 중 두번 째로 작은 값 구하기
1. 원래한 생각:
- dictionary indexing 통해서 빠르게 빈도를 count 한다.
- dict 를 배열로 바꿔서, 빈도수 기준 내림차순 정렬 후 , value 기준 오름 차순 정렬한다
```python
dic = {arr: 0 for arr in set(array)}
for arr in array:
    dic[arr] += 1

count = [[k, v] for k, v in dic.items()]
count.sort(key = lambda x:x[0])
count.sort(key = lambda x:x[1],reverse=True)
```
2. Counter libaray 사용
```python
from collections import Counter
count = Counter(array) # array에서 빈도수를 count해서 dic 형태로 반환한다.
count = count.most_common() # dic에서 빈도수 높은 순으로 정렬해서 리스트로 반환한다.
```
3. 절댓값이 4000을 넘지 않으므로 계수 정렬 이용 방법