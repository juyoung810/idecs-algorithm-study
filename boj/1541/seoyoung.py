### 잃어버린 괄호
## 양수와 +,- 그리고 괄호를 가지고 식을 만들고, 괄호 모두 지움. 괄호를 적절히 쳐서 값을 최소로 만들기.

expression = input()

# -를 기준으로 수를 나누기. 나눠진 안에서 수끼리 더하고 전체 빼기

minus = expression.split("-")
elements = []

for plus in minus:    # 반복문 두번. 시간복잡도 O(N^2)
    num_list = plus.split("+")
    result = 0
    for num in num_list:
        result += int(num)
    elements.append(result)

total = elements[0] - sum(elements[1:])

print(total)