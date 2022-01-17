import sys
input = sys.stdin.readline

N = int(input())
dict = {}
for i in range(N):
    x, y = input().strip().split(".") # strip으로 공백 제거
    if y in dict:
        dict[y] += 1
    else:
        dict[y] = 1
for key in sorted(dict.keys()):
    print(key, dict[key])

print(sorted(dict.keys()))
print(sorted(dict.items()))


########################################################
# import sys

# n = int(sys.stdin.readline())
# ext_dict = {}
# for i in range(n):
#     _, ext = sys.stdin.readline().rstrip().split(".")
#     if ext_dict.get(ext):
#         ext_dict[ext] += 1
#     else:
#         ext_dict[ext] = 1
# for key in sorted(ext_dict.keys()):
#     print('{} {}'.format(key, ext_dict[key]))