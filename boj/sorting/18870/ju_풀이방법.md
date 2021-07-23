# boj 18870: 좌표 압축
> 문제 주소: https://www.acmicpc.net/problem/18870
> 
> silver 2

## 문제 해결 방법
1. 입력 받은 배열을 중복 제거 후 정렬한다.
2. 해당 배열을 입력 받은 value순으로 출력하기 위해 dictionary 형태로 만든다.
key = 입력받은 value, value = 정렬된 list 에서 index(자기 보다 작은 것의 갯수를 나타낸다)
   
3. 입력받은 value 순서로 dic에 key로 접근해서 저장된 index를 출력한다.
```python
n = int(input())
arr = list(map(int, input().split()))
# set를 이용해서 중복을 제거 해준 후 list로 바꿔서 정렬한다.
arr2 = sorted(list(set(arr)))

# 중복이 없어진 value :  index (순서)를 저장한다.
dic = {arr2[i] : i for i in range(len(arr2))}

# dic[key] = value 이므로, arr 안의 값을 key로 value를 출력해준다.
for i in arr:
    print(dic[i],end = " ")
```

### 시간 복잡도
dictionary indexing으로 시간 복잡도를 줄일 수 있다.

### 새로 알게된 점
1. 중복 제거시 `set()` 통해 집합으로 제거
2. `dictionary index` 통해 쉽고 빠르게 접근 가능