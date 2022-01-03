N = int(input())
cf_tm = []
for _i in range(N):
    _cf = list(map(int, input().split()))
    cf_tm.append(_cf)
cf_tm.sort(key=lambda x: (x[1], x[0]))
ed_tm = 0
count = 0
for i in range(N):
    if cf_tm[i][0] >= ed_tm:
        count += 1
        ed_tm = cf_tm[i][1]
print(count)

# # #############################################################
# 따온 코드
n = int(input())
l = sorted(sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0]), key=lambda x: x[1])

count = 0
last = 0
for a, b in l:
    if last <= a:
        count += 1
        last = b
print(count)

                
    
    
    
    

            