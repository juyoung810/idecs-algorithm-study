s = input()
cnt0 = 0
cnt1 = 0

if s[0] == '1':
    cnt0 += 1
else:
    cnt1 += 1

for i in range(1, len(s) -1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))