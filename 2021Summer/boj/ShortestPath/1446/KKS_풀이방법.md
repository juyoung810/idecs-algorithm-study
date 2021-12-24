# boj 1446 : 지름길 by KKS
> 문제 주소: https://www.acmicpc.net/problem/1446
> 
> 난이도: silver 1

## 1.문제설명
- 주어지는 입력: 지름길 개수 N, 고속도로의 길이 D
- 0부터 D까지 가야한다 중간중간에 지름길이 있음
- 지름길의 정보는 (지름길 시작지점, 지름길 종료지점, 지름길의 거리)
- 이때 D까지의 가장 빠른 이동거리를 구하는 것

## 2. 문제 접근법 
- distance 리스트에 i번째 인덱스까지의 최단거리를 저장
- i를 순서대로 증가시키면서 해당 인덱스의 거리를 이전 인덱스와 비교해봄
```python
distance[i] = min(distance[i], distance[i-1]+1)
```
- 지름길의 시작점에 도착하면 지름길 이용
```python
    for s, e, d in short_cut:
        if i == s and e <= D and distance[i]+d < distance[e]:
            distance[e] = distance[i]+d
```

## 3.문제 해결 아이디어 or 핵심
- 완전히 다익스트라다! 라고 할수는 없지만
- 거리를 업데이트 해주는 것이 핵심

## 4.특별히 참고할 사항
- 변수이름을 사용하는데 주의하도록하다
- D와 d 구분하는걸 까먹어서 계속 오류가 났다

## 5.코드구현
``` python
N, D = map(int, input().split())
short_cut = [list(map(int, input().split())) for _ in range(N)]
distance = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for s, e, d in short_cut:
        if i == s and e <= D and distance[i]+d < distance[e]:
            distance[e] = distance[i]+d
print(distance[D])
```