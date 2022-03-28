case = int(input())

for i in range(case):
    n = int(input())
    phone = []
    for j in range(n):
        phone.append(input())
    phone.sort()
    for k in range(n):
        if k == (n-1):
            print("YES")
            break
        if phone[k] == phone[k+1][0:len(phone[k])]:
            print("NO")
            break
