n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
best_price = min(price) #nlogn
ans = 0
cur_loc = 0

def find_smaller(cur_loc, price):
    _temp = cur_loc
    for _temp in range(cur_loc, n):
        if price[_temp] < price[cur_loc]:
            return _temp
#특정도시 방문 -> 가격이 제일 저렴하다? -> 다 사버린다
#제일 저렴한 가격 아님 -> 다음도시보다 비싸다? -> 거리만큼만 삼
#다음 도시보다 싸다 -> 자기보다 싼 가격 나올때까지 삼 다 삼

while cur_loc < n:
    if price[cur_loc] == best_price:
        ans += sum([best_price * item for item in distance[cur_loc:]])
        break
    else:
        if price[cur_loc] >= price[cur_loc+1]:
            ans += distance[cur_loc] * price[cur_loc]
            cur_loc += 1
        else:
            smaller = find_smaller(cur_loc, price)
            ans += sum([price[cur_loc] * item for item in distance[cur_loc:smaller]])
            cur_loc = smaller

print(ans)

