### boj 1475: 방번호
> 문제 주소:  https://www.acmicpc.net/problem/1475


#### 문제 해결 방향
6,9 를 뒤집어서 사용가능하므로 (6이 쓰인 수 + 9가 쓰인 수) 를 2로 나눈 몫과 나머지를 더하면 6,9로 고려한 필요한 set 수가 나온다.

- 필요한 각각의 수의 갯수를 알기 위해 해당 수를 index로 가지는 count 배열을 만든다

        num_set = [0] * 10

- 각각의 수가 필요한 갯수를 count 한다.
  
        for i in room:
            num_set[int(i)] += 1
- 6, 9 만으로 필요한 set수를 먼저 구한다.

        count = (num_set[6] + num_set[9]) // 2 + (num_set[6] + num_set[9]) % 2

- 이미 정해진 set 수를 벗어나서, 더 필요한 세트 수를 구한다.


    for i in range(len(num_set)):
        if i != 6 and i != 9 :
            if num_set[i] - count > 0:
                count += num_set[i] - count
