## boj 11399: ATM
> 주소: https://www.acmicpc.net/problem/11399


### 문제 해결 방향
- 각각의 사람 별로 주어진 시간에 대해서 , 오름 차순으로 정렬했을때 가장 작은 총 시간이 걸리는 것을 알 수 있다.
- 시간을 누적합을 list 로 나타내고, 해당 list 를 더한다.

        p.sort()
        sum_num = 0
        for i in range(N):
            p[i] += sum_num
            sum_num = p[i]

### 시간 복잡도
- 파이썬 list의 sort() 함수의 시간 복잡도 : O(NlogN)
