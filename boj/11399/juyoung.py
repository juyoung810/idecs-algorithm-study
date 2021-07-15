import sys

N = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split(" ")))

# p 오름 차순 정렬
p.sort()
sum_num = 0
for i in range(N):
    p[i] += sum_num
    sum_num = p[i]

sys.stdout.write(str(sum(p)))