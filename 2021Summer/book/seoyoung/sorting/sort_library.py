### 파이썬의 정렬 라이브러리 sorted()는 병합 정렬 기반으로 만들어졌다. 최악의 경우에도 O(NlogN) 보장
### 리스트 객체의 내장 함수 sort()도 있다. 내부 원소가 바로 정렬된다.

# 정렬 라이브러리에서 key를 활용한 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)   # 키 값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 된다.
print(result)

## 정렬 라이브러리의 시간 복잡도는 항상 최악의 경우에도 시간복잡도 O(NlogN)을 보장


### 코딩 테스트에서 정렬 알고리즘이 사용되는 경우
## 1. 정렬 라이브러리로 풀 수 있는 문제
## 2. 정렬 알고리즘의 원리에 대해서 물어보는 문제 : 선택 정렬, 삽입 정렬, 퀵 정렬 드으이 원리를 알고 있어야 함
## 3. 더 빠른 정렬이 필요한 문제 : 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적 개선 필요
