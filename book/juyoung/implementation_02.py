import datetime

start_time = datetime.datetime.now()

# 총 데이터 수: 24 * 60 * 60 = 86400 개
# 데이터 수 백만개 이하면 완전 탐색!!
N = int(input())
count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
# ms
ms_elapsed_time = elapsed_time.microseconds / 1000
print(str(ms_elapsed_time))
