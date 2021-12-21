# <span style="color:red" >boj 12015: 가장 긴 증가하는 부분 수열 2 by juyoung </span>
> 문제 주소: https://www.acmicpc.net/problem/12015
> 
> gold 2

## 최장 증가 부분 수열 알고리즘
> 최장 증가 부분 수열(LIS, Longest Increasting Subsequence)

- 원소가 n개인 배열의 일부 원소를 골라내서 만든 부분 수열 중,
  각 원소가 이전 원소보다 크다는 조건을 만족하고,
  그 길이가 최대인 부분 수열
  - ex) {6,2,5,1,7,4,8,3} => LIS = {2,5,7,8}
  - 증가하는 부분 수열 중 가장 긴 것  
    
### 1. 간편한 방법 : DP 이용 - 동적계획법 : O(N^2)
- 각 index 별 해당 index에서 끝나는 최장 증가 부분 수열의 길이를 구한다.
```python
length = [] # 인덱스 마다 각 증가 수열의 길이
length.append(1) # 0 번째 index 의 증가 수열의 길이는 당연히 1
for i in range(1,N):
    length.append(1)
    for j in range(i):
        
        if arr[i] > arr[j] and legth[i] < length[j] + 1:
            length[i] = length[j] + 1
```
- 주어진 배열에서 index 하나씩 늘려가면서 확인한다.
- i의 index 보다 작은 index의 값을 확인해서, i 보다 작은 값일 경우 , lenth를 update 해준다.
- length update 의 기준
    - 기존 i index 가 가진 lenth[i]의 길이에 +1 한 것과
    - 원래 기존 i의 길이와 비교한다. 
    - __ 둘 중에 더 큰 값으로 lenth[i] 값을 update 한다.
    - ex) 10,20,10,30 이 있다고 하면, 
        - 10 -> legth[0] = 1
        - 20 -> legth[1] = legnth[0] + 1 > 1 = 2
        - 10 -> legth[2] = 1
        - 30 -> legth[3] = legth[0] + 1 > 1 = 2, 
                            legth[1] + 1 > 2 = 3,
                            legth[2] + 1 < 3 = 3
  
### 2. LIS 의 길이를 구하기 위해 이분 탐색을 활용한다. (이분탐색 활용한 LIS 구하기) : O(NlogN)
- 시간복잡도 개선 위해 LIS 에 각 요소를 삽입할 때, 위치를 구하기 위해 이분 탐색을 활용한다.
- 주어진 배열의 인덱스를 찾아보면서, 그 숫자가 들어갈 위치를 이분 탐색으로 탐색해서 넣는다.
1. lis[0]에 array[0]의 값을 삽입한다.
2. 만약 array[1]의 값이 lis에 들어간 마지막 값보다 큰 경우 append 하고 길이가 늘어난다.
3. 만약 array[1]의 값이 lis에 들어간 마지막 값보다 작거나 같은 경우 binarySearch를 이용해, 들어갈 위치를 찾는다.
4. 찾은 위치의 index에 값을 update 한다.
5. lis 의 길이가 lis 가 된다.
```python
def binarySearch(lis,target):      
    start = 0                      
    end = len(lis)-1               
    while start <= end:            
        mid = (start + end) //2    
        if lis[mid] == target:     
            return mid             
        elif lis[mid] > target:    
            end = mid -1           
        else: start = mid +1       
                                   
    return start                   
lis = []                                                                
lis.append(array[0])                                                    
length = 1                                                              
for i in range(1, N):                                                   
    if array[i] > lis[length]:                                          
        # lis 에 들어있는 가장 마지막 값보다 큰 경우, 바로 맨 뒤에 넣는다.                      
        lis.append(array[i])                                            
        length+=1                                                       
    # lis에 들어갈 수 있는 해당 원소의 위치를 찾는다. -> 이분탐색                             
    else:                                                               
        lis[binarySearch(lis,array[i])] = array[i]                      
                                                                        
                                                           
sys.stdout.write(str(length))                                           
                                                                                                          
```
- 주의: binarySearch를 재귀를 통해 구현할 경우 시간이 더 걸린다.
- 이미 존재하는 값의 위치를 찾는 것이 아닐 경우 start >= end 까지 이므로 start 위치에 넣으면 맞는 위치이다.
- __lis 알고리즘의 길이만 알 수 있고, 구성하는 요소는 알 수 없다.__