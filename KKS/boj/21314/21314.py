num = input()
min, max = '', ''
cnt = 0

for n in num:
    if n == 'M':
        cnt += 1
    else:
        if cnt > 0:
            min += str((10 ** cnt)+5)
            max += str(5 * (10 ** cnt))
        else:
            min += '5'
            max += '5'
        cnt = 0

if cnt > 0:
    min += str(10 ** (cnt-1))
    max += '1' * cnt

print(max)
print(min)