text = input()
bomb = list(input())
stk = []
#answer = ''

for i in text:
    stk.append(i)
    if len(stk) >= len(bomb):
        if bomb[-1] == i:
            if stk[-len(bomb):] == bomb:
                for j in range(len(bomb)):
                    del stk[-1]

if len(stk) == 0:
    print("FRULA")
else:
    print(''.join(stk))
    # for i in stk:
    #   answer += i
    # print(answer)