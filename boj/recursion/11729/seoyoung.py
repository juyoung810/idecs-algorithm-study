### 하노이 탑 이동 순서
## 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
## 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
## 첫 번째 장대에서 세 번째 장대로 모든 원판을 최소한의 이동 횟수로 옮기려 할 때 필요한 이동 순서를 출력하라!

n = int(input())

# 가장 큰 걸 목표 기둥으로 옮겨야 함! 그 과정을 계속 반복한다.

def hanoi(n, s_tower, f_tower, m_tower):
    # 재귀함수를 만들때는 종료 조건을 만들어줘야 한다!!!!!!
    if n == 1:
        print(s_tower, f_tower)
        return     # 1이면 종료
    # 가장 큰 하나 남기고 중간 기둥으로 옮기기
    hanoi(n-1, s_tower, m_tower, f_tower)
    # 가장 큰 하나 마지막 기둥으로 옮기기
    print(s_tower,f_tower)
    # 중간 기둥에 있는 거 전체를 마지막 기둥으로 옮기기
    hanoi(n-1, m_tower, f_tower, s_tower)


print(2**n-1)
hanoi(n, 1, 3, 2)