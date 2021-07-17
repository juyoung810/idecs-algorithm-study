### boj 1966: 프린터 큐
> 문제 주소: https://www.acmicpc.net/problem/1966


#### 문제 핵결 방향
- 처음 입력 받았을 때 (각각의 index, 중요도 tuple) 을 저장한다

      paper = []
      count = 0
      # 큐 만들기
      for i in range(N):
        paper.append((i,priority[i]))

- 존재하는 큐에서 가장 중요도가 큰 문서의 중요도 보다 크거나 같을 때 pop 하고 빠져나온 paper의 수를 count 한다.
- 빠져나온 paper의 index가 궁금한 문서의 index와 같을 때 종료한다.
- 가장 중요도가 큰 문서가 아닐 경우 가장 마지막으로 이동한다.

      while True:
        max_priority = max(paper, key= lambda x:x[1])
        if paper[0][1] >= max_priority[1]:
            if paper.pop(0)[0] == M:
                count+=1
                print(count)
                break
            else: count+=1
        else:
            paper.append(paper.pop(0))
  