# <span style="color:red" >boj 2352: 반도체 설계 by juyoung </span>
> 문제 주소: https://www.acmicpc.net/problem/2352
> 
> gold 2

## 문제 해결 방향
- A[1]  - B[4] 가 연결되면, 꼬이면 안되기 때문에 B[5]또는 B[6]에만 연결할 수 있다.
- A[i] 포트 -- B[j] 포트로 연결할려고 할 때, 현재 B에 연결되어 있는 포트 중 가장 큰 것 보다 작은 경우에는
연결할 수 없다.
- __따라서 B에 연결해야하는 포트들 중에서 연속적으로 증가하는 수의 최대 길이를 구한다.__
  -> LIS : 최장 증가 부분 수열을 찾는 문제
  


