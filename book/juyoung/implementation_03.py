import datetime

start_time = datetime.datetime.now()

x_types = ['a','b','c','d','e','f','g','h']
y_types = ['1','2','3','4','5','6','7','8']

# 문자 단위로 나누기
x,y = list(input())

count = 0
# 0 ~ 7
x_index = x_types.index(x)
y_index = y_types.index(y)

# 총 8가지 경우
steps = [(+2,-1),(+2,-1),(+2,+1),(+2,-1),
         (+1,+2),(+1,-2),(-1,+2),(-1,-2)]

for step in steps:
    nx = x_index + step[0]
    ny = y_index + step[1]
    if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
        count +=1
print(count)



end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
# ms
ms_elapsed_time = elapsed_time.microseconds / 1000
print(str(ms_elapsed_time))

# 428.765ms