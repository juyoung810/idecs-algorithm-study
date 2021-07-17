# (1 ~N),(1~N)
import sys
import datetime

start_time = datetime.datetime.now()
N = int(sys.stdin.readline())

plans = list(map(str,sys.stdin.readline().split()))

#(y,x)
# L,R,U,D
dx = [-1,1,0,0]
dy = [0,0,-1,+1]

move_types = ['L','R','U','D']
x = 1
y = 1
#(Y,X)
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x,y = nx,ny

sys.stdout.write(str(y) + " " + str(x) + '\n')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
# ms
ms_elapsed_time = elapsed_time.microseconds / 1000
sys.stdout.write(str(ms_elapsed_time))

#3 4
#3.508ms


