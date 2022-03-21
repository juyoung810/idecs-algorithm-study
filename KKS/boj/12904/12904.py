input_str = list(input())
target = list(input())
while len(target) > len(input_str):
    if target[-1] == 'A':
        target.pop()
    else:
        target.pop()
        target.reverse()
if target == input_str:
    print(1)
else:
    print(0)
