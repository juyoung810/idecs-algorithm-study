n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #오름차순
b.sort(reverse=True) #내림차순

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: # 오름차순에서의 원소보다 내림차순의 원소가 작으면 그 뒤로는 비교할 필요없음 -> 오름차순에서는 더 커질꺼고 내림차순에서는 더 작아질꺼임
        break

print(sum(a))