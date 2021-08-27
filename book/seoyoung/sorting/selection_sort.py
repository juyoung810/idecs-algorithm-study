'''
< 선택 정렬(selection sort)>
가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고 그다음 작은 데이터를 선택에 앞에서 두 번째 데이터와 바꾸는 과정 반복
매번 가장 작은 것을 선택. 선택 정렬 알고리즘
가장 작은 데이터를 앞으로 보내는 과정을 n-1번 반복하면 정렬 완료
현재 데이터의 상태와 상관없이 무조건 모든 우너소를 비교하고 위치를 바꾼다
'''

# 선택 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  #가장 작은 원소의 인덱스. 시작은 맨 앞
    for j in range(i+1, len(array)): # 가장 작은거 다음에 대해서
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 자리를 바꿔준다.

print(array)

## 선택 정렬의 시간복잡도는 O(N^2). 반복문이 얼마나 중첩되었는지를 기준으로 간단히 시간 복잡도 판단 가능
## 비효율적이지만, 특정 리스트에서 가장 작은 데이터를 찾을 때 필요함