## boj 12904 : A와 B
> 문제 주소 : https://www.acmicpc.net/problem/12904
>
> 난이도 : Gold 5

### 0. 문제
- A와 B로만 이루어진 영어 단어 존재.
- 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임
- 문자열 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.
1. 문자열의 뒤에 A를 추가한다.
2. 문자열을 뒤집고 뒤에 B를 추가한다.
- 주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램 작성하라.


### 1. 문제 해결 방향
- 두 가지 연산 중에서 언제 어떤걸 써야하는지 알아야함
- S -> T 를 확인하는 건 너무 경우의 수가 많음. T -> S가 될 수 있는지 확인
- T[-1] == A 면 A를 뺀다. T[-1] == B 면 B를 빼고 뒤집는다.

### 2. 소스코드
- 문자열을 입력받는다.
```python
import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())
```
- switch를 통해 T가 S가 될 수 있는지 여부를 확인한다.
- T가 아직 남아있는 동안 계속 확인해본다.
- T의 마지막 문자를 확인해서 바꿔주고, T와 S가 같으면 switch를 True로 바꿔준다.
```python
switch = False
while T:
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
    if T == S:
        switch = True
        break

if switch:
    print(1)
else:
    print(0)
```


### 3. 알아둘 점
- sys.stdin.readline으로 input 받을 때는 rstrip() 해주는 것을 잊지 말자