### 숫자 카드 게임
## 여러 개의 숫자 카드중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
## N X M 형태의 카드. 뽑고자 하는 카드 포함된 행 선택. 가장 숫자 낮은 카드 뽑기
## 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

# 입력조건 : 첫째 줄에 숫자 카드들이 놓인 행의 개수 n과 열의 개수 m이 공백을 기준으로 하여 각각 자연수로 주어짐
n, m = map(int, input().split())

# 둘째 줄부터 n개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어짐.
max_num = 0

for i in range(n):   # 행 수만큼 반복.
    data = list(map(int, input().split()))  # 한 줄씩 입력받기
    min_num = min(data)  # 행에서 가장 작은 숫자
    max_num = max(max_num, min_num)  # 지금까지 저장된 가장 큰 수보다 크면 교체

print(max_num)
