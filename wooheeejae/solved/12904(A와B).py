S = list(input())
T = list(input())


while True:
    if T[-1] == 'A':
        del T[-1]
    elif T[-1] == 'B':
        del T[-1]
        T.reverse()
    if S == T:
        print(1)
        break
    if len(T) == 0:
        print(0)
        break
