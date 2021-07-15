## boj 11047: 동전 0
> 주소: https://www.acmicpc.net/problem/11047


### 문제 해결 방향
- 가장 큰 수로 부터 K를 만들어야 동전의 갯수가 최소가 된다.
- 오름 차순으로 주어지므로 list.pop()함수를 이용해서 가장 큰 값부터 빼낸다.
- K // coin의 value 이 몫이 해당 value 로 만들어지는 K이내의 수 이고, K % coin이 남은 돈이 된다.
        

        count = 0
        while K > 0:
            coin = coins.pop()
            if K // coin != 0:
                count += K // coin
                K = K % coin