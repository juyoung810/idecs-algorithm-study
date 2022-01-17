# collections 모듈의 Counter 클래스
> 데이터의 개수를 셀 때 유용한 클래스
> 
> 참고: https://www.daleseo.com/python-collections-counter/

# 사용 방법
`from collections import Counter`

## 카운팅
```python
from collections import Counter

Counter('hello world')
#Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

```
## 특징
- 사전(dict)를 확장하고 있어 사전에서 제공하는 API 모두 사용 가능 

###[Dictionaries: dict and defaultdict]
> https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
                       
| 연산             | 예제          | 시간복잡도       | 참고                                                            |
|----------------|-------------|-------------|---------------------------------------------------------------|
| Index          | d[k]        | O(1)	       |                                                               |
| Store          | d[k] = v    | O(1)	       |                                                               |
| Length         | len(d)      | O(1)	       |                                                               |
| Delete         | del d[k]    | O(1)	       |                                                               |
| get/setdefault | d.get(k)    | O(1)	       |                                                               |
| Pop            | d.pop(k)    | O(1)	       |                                                               |
| Pop item       | d.popitem() | O(1)	       | '랜덤하게' 고른 item pop                                            |
| Clear          | d.clear()   | O(1)	       | s = {} 또는 s = dict() 와 유사                                     |
| View           | d.keys()    | O(1)	       | d.values() 도 같다.                                              |
| Construction   | dict(...)   | O(len(...)) | (key,value) tuple의 갯수에 달렸다.                                   |
| Iteration      | for k in d: | O(N)        | all forms: keys, values, items<br/> Worst: no return/break in loop | 


=> 따라서 대부분의 dictionary 연산은 O(1)

## 연산
### - elements() : count한 갯수 만큼 요소 보여준다
- 1보다 적으면 무시된다.
```python
c = Counter(a=4, b=2, c=0, d=-2)
sorted(c.elements())
# ['a', 'a', 'a', 'a', 'b', 'b']
```
### - most_commons([n]) : count 한 것 중 가장 큰 n개의 요소 list 반환
- n이 생략될 경우 데이터 갯수 많은 순 정렬
```python
Counter('abracadabra').most_common(3)
# [('a', 5), ('b', 2), ('r', 2)]
```
### - subtract([iterable-or-mapping])
- `dict.update()` 와 유사
- 값을 replace 하지않고 count 갯수를 뺀다
```python
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
# Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
```

### - total()
- count 한 것의 총 합
```python
c = Counter(a=10, b=5, c=0)
c.total()
# 15
```
### 추가 기능
| 연산                          | 설명                               |
|-----------------------------|----------------------------------|
| c.total()                   | count 수 모두 더한다.                  |
| c.clear()                   | count 모두 reset                   |
| list(c)                     | unique 요소의 list                  |
| set(c)                      | set으로 변환                         |
| dict(c)                     | dict 형으로 변환                      |
| c.items()                   | (elem, cnt) 를 리스트로 반환            |
| Counter(dict(list_of_pairs)) | (elem, cnt) pair를 Counter 형으로 변환 |
| c.most_common()[:-n-1:-1]   | n개의 가장 많은 element                |
| +c                          | 0 또는 음수 count 제거                 |
