
room = list((input()))
num_set = [0] * 10

for i in room:
    num_set[int(i)] += 1

# 6, 9 만으로 필요한 set 수
count = (num_set[6] + num_set[9]) // 2 + (num_set[6] + num_set[9]) % 2


for i in range(len(num_set)):
    if i != 6 and i != 9 :
        if num_set[i] - count > 0:
            count += num_set[i] - count



print(count)