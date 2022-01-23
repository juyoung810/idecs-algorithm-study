import sys
from collections import defaultdict
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
name_dict = defaultdict(int)
for i in range(N):
    name = input().rstrip()
    name_dict[name] += 1
for i in range(M):
    name = input().rstrip()
    name_dict[name] += 1
name_list = [item for item in name_dict.items() if item[1] > 1]
name_list.sort(key= lambda x : x[0])
print(len(name_list))
for item in name_list:
    print(item[0])