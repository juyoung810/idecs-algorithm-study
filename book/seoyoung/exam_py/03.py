'''
< 문자열 뒤집기 >
0과 1로만 이루어진 문자열 s에 있는 모든 숫자를 전부 같게 만들려고 한다. 연속된 하나 이상의 숫자를 잡고 모두 뒤집는다.
문자열이 주어졌을 때, 해야 하는 행동의 최소 횟수를 출력하라.
달라지는 지점을 발견해서 추가하고,
'''

s = input()

count_0 = 0
count_1 = 0

if s[0] == '0':
    count_0 += 1
else:
    count_1 += 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            count_0 += 1
        else:
            count_1 += 1

print(min(count_0, count_1))


# zero = 0
# one = 0
# bf = s[0]
# af = s[0]
#
# for i in range(len(s)):
#     if i == len(s):
#         if s[i] == '0':
#             zero += 1
#         else:
#             one += 1
#         break
#     af = s[i]
#     if bf == af:
#         continue
#     else:
#         if bf == '0':
#             zero += 1
#         else:
#             one += 1
#     bf = af
#
# print(min(zero, one))


s = input()
s = s.split('1')

one = s.count('')
print(one)
zero = len(s) - one

print(min(zero, one))