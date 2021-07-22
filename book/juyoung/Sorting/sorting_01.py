# 위에서 아래로

N = int(input())
array = []
for _ in range(N):
    num = int(input())
    array.append(num)

# array.sort()
# array.reverse()

# 파이썬의 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array,reverse=True)
for i in array:
    print(i,end = " ")
