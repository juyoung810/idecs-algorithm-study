# 정렬 (Sorting)
> 데이터를 특정한 기준에 따라서 순서대로 나열한다.
- 이진 탐색(Binary Search 의 전처리 과정)
- 선택정렬, 삽입 정렬, 퀵정렬, 계수 정렬
- 알고리즘의 효율성
- 상황에 따라 적절한 정렬 알고리즘 사용
- 리스트를 뒤집는 연산 : `O(N)` (오름차순 -> 내림차순 ,내림차순 -> 오름차순 시 유용하게 사용)
---
## 1. 선택 정렬 : O(N^2)
> 가장 작은 것을 선택한다.
- 가장 작은 데이터를 선택해서 맨 앞과 바꾸고, 그 다음으로 작은 데이터를 선택해서 앞에서 두번째 데이터와 바꾸는 과정 반복
- 가장 작은 데이터 선택해 앞으로 보내는 과정 O(N-1) 번 반복
- 스와프: 두 원소의 위치 바꾸는 방법 in python `array[i],array[j] = array[j],array[i]`
```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): # O(N-1) 번 반복
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index],array[i] # swap
```
---
## 2.  삽입 정렬: O(N^2) -> 거의 정렬된 상태일 경우 매우 빠르다. 최선의 경우: O(N)
> 특정한 데이터를 적절한 위치에 '삽입' 한다.
- 선택 정렬에 비해 효율적이다.
- 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
- 적절한 위치를 찾아서 삽입한다.
- 첫 번째 데이터는 그 자체로 이미 정렬되어 있다고 가정하기 때문에, 두번째 데이터부터 시작한다.
- 적절한 위치에 삽입하는 과정 N-1 번 반복
- __거의 정렬된 상태에서는 퀵 정렬보다 강력__
```python
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array)):
    # i 부터 시작해서 까지 감소하여 반복하는 문법
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else: break # 자기보다 작은 데이터를 만나면 stop
    
```
---
## 3. 퀵 정렬 : O(NlogN)
> 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까?
- 가장 많이 사용되는 알고리즘
- 정렬 라이브러리의 근간 
__- `피벗(pivot)` : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'__
- 퀵 정렬 수행하기 전에 , 피벗을 어떻게 설정할 지 명시해야한다.
__- `호어 분할(Hoare Partition)` : 리스트에서 _첫 번째 데이터_ 를 피벗으로 정한다.__
- 퀵 정렬은 전체를 3개의 파트로 나눠서 보는게 편하다.

1. <파트1> : __분할하기__
- 피벗을 기준으로 왼쪽에서 부터 [피벗 다음 ~ 피벗보다 작은 데이터] 를 찾고, 오른쪽에서 부터 [끝 ~ 피벗보다 큰 데이터] 를 찾는다. 
- 만약 왼쪽에서 찾는 값과 오른쪽에서 부터 찾는 값의 위치가 __엇갈린 경우__ '작은 데이터'와 '피벗'의 위치를 변경한다.
- 엇갈리지 않은 경우 '작은 데이터' 와 '큰 데이터'를 변경한다.
2. <파트2> : 분할 후 왼쪽 part 또 퀵 정렬하기
3. <파트3> : 분할 후 오른쪽 part  또 퀵 정렬하기

#####-> 재귀 함수와 동작 원리가 같다. 종료조건: 리스트의 원소가 1개인 경우 이미 정려되어 있다고 간주하며 분할 불가능
- 직관적인 형태의 퀵 정렬 소스 코드
```python
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end: #원소가 1개 이하면 종료
        return
    pivot = start # 첫 번째 원소를 pivot으로 지정
    left = start +1 
    right = end
    # 분할할 때 까지 반복 == 엇갈릴 때 까지 반복
    while left <= right:
        # 피벗보다 큰 데이터 찾을 때 까지 반복
        while left <= end and array[left]  <= array[pivot]:
            left +=1
        # 피벗보다 작은 데이터 찾을 때 까지 반복
        while right >= start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈린 경우 -> 분할 -> pivot 보다 작은 데이터와, pivot 바꾼다. 
        if left > right:
            array[pivot],array[right] = array[right],array[pivot]
        # 엇갈리지 않은 경우 -> 작은데이터 , 큰 데이터 바꾼다.
        else: array[left],array[right] = array[right],array[left]
        
    
        # 분할 이후 분할 왼쪽 리스트 또 quick 정렬
        quick_sort(array,start,right-1)
        quick_sort(array,right +1,end)
quick_sort(array,0,len(array)-1)
```

- python 장점 살려 짧게 쓴 코드
```python
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트의 원소의 갯수가 1보다 작으면 종료
    if len(array) <= 1:
        return
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in range(tail) if x<=pivot] # 분할된 왼쪽 부분
    right_side = [x for x in range(tail) if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

quick_sort(array)
    
```
### 시간 복잡도
- 평균 : O(NlogN) - 항상 정확히 반씩 나눈다고 가정했을 때: __무작위로 값 들어올 경우 효율적__
- 최악 : __O(N^2) : 정렬된 상태로 들어온 경우__
- __정렬 라이브러리는 O(NlogN) 이 보장된다.__

---
## 4. 계수 정렬
> 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때
> 모든 범위를 담을 수 있는 크기의 리스트를 선언
- __특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘__
- 가장 큰 데이터와 가장 작은 데이터의 차이가 `1,000,000` 를 넘지 않을 때
- __데이터 개수 N, 데이터 중 최대값이 K 일 때 최악의 경우에도 수행시간 `O(N+K)` 보장__
- 값을 비교한 뒤에 위치를 변경하며 정렬하는 방식(비교 기반의 정렬 알고리즘)이 아니다.
- 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다.
- 0~9 까지 데이터 있으면 9+1 크기의 리스트 선언
- __데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.__
```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모두 0 으로 초기화)
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
```
- __계수 정렬은 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을수록 유리하며 항상 사용할 수는 없다.__
- 공간복잡도: O(N+K)
---
## 5. 파이썬의 정렬 라이브러리 : O(NlogN)
> 기본 정렬 라이브러리인 sorted() 함수 제공 - 퀵정렬과 동작 방식 비슷한 병합 정렬로 만들어짐 
- 리스트, 딕셔너리 자료형 입력받아 정렬된 _리스트 자료형_ 반환
- 리스트 객체 내장 함수 __sort()__  이용해 리스트 변수 내부 원소 바로 정렬 가능
- __sorted(), sort() 모두 정렬의 기준이 되는 key 값 매개 변수로 입력 받을 수 있다.__
```python
array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array,key = setting)
```
- 매개 변수 key 값 혹은 _lambda 함수_ 사용 가능
```python
array = sorted(array, key = lambda student:student[1])
```
- 내림 차순으로 정렬하고 싶은 경우 
```python
array = sorted(array,reverse=True)
```
---
## <정리>
- 별도의 요구 없이 단순히 정렬해야하는 상황에서 기본 정렬 라이브러리 사용
- 데이터의 범위가 한정되어 있으며 더 빠르게 동작해야 할 때는 계수 정렬 사용

##### 3가지 정렬 알고리즘 문제 유형
1. __정렬 라이브러리로 풀 수 있는 문제__: 단순히 정렬 기법을 알고 있는지 물어보는 문제
2. __정렬 알고리즘의 원리에 대해서 물어보는 문제__: 선택정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알아야 풀 수 있는 문제
3. __더 빠른 정렬이 필요한 문제__: 퀵 정렬 기반의 정렬기법으로 풀 수 없으며 계수 정렬등의 다른 정렬 알고리즘을 이용하거나,
   문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.