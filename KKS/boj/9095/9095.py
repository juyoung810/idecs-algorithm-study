T = int(input())
question = []
for i in range(T):
    question.append(int(input()))
cache = [1e9] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4
for i in range(4,11):
    cache[i] = (cache[i-1]) + (cache[i-2]) + (cache[i-3])
for q in question:
    print(cache[q])