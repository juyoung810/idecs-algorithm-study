# boj 2108: 통계학
> 문제 주소: https://www.acmicpc.net/problem/2108

### 문제설명
- 리스트 입력받고
- 산술평균, 중앙값, 최빈값, 범위구하기

### 최빈값 구하는방법
- 나머지는 간단하게 구할수 있고 최빈값을 어떻게 구하는지 중요
- Counter 라이브러리 사용
산업공학실험에서 조교님이 수업시간에 알려준 부분인데 실제로 쓸줄은 몰랐다.
``` python
#최빈값 -> counter 사용
cnt = Counter(data) #원소별로 개수를 세서 딕셔너리 형태로 반환
cnt = cnt.most_common() #count수가 높은순서대로 정렬해서 리스트 형태로 반환
if len(cnt) > 1: 
    if cnt[0][1] == cnt[1][1]: #동일한 최빈값이 있으면
        print(cnt[1][0]) #두번째로 작은 값 반환
    else:
        print(cnt[0][0]) #동일한 최빈값 없으면 첫번째 최반값 반환
else:
    print(cnt[0][0]) #수가 한개밖에 없을떼
```