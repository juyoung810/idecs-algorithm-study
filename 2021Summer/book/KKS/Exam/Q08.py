n = input()
char = []
nums = 0
for item in n:
    if item.isalpha():
        char.append(item)
    else:
        nums += int(item)
char.sort()
if nums != 0:
    char.append(str(nums))
print(''.join(char))
