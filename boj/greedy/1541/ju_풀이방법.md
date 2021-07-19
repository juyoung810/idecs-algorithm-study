## boj 1541: 잃어버린 괄호
> 주소: https://www.acmicpc.net/problem/1541


### 문제 해결 방향
- (-)단위로 나눠서, 모든 덩어리를 각각 더한 다음 모두 처음 숫자에서 부터 뺀다면, 최소의 수가 될 것이다.
- str 입력받고, '\n' 문자 제외한 다음, - 단위로 나눠주기
    
        eq = sys.stdin.readline().rstrip('\n').split('-')
- 나눈 덩어리를 + 단위로 나누고, 모두 더하기

        for i in range(len(eq)):
        eq_num = list(map(int,(eq[i].split("+"))))
        eq[i] = sum(eq_num)

- 모든 덩어리를 처음 값에서 - 한다.
    
        result = eq[0]
        for i in range(1,len(eq)):
            result -= eq[i]
        
        sys.stdout.write(str(result))
