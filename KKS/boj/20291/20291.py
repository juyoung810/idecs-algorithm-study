import sys
input = sys.stdin.readline
N = int(input())
from collections import Counter
files = []
for i in range(N):
    _, extension = input().rstrip().split('.')
    files.append(extension)
count_dict = Counter(files)
count = sorted(count_dict.items(), key = lambda x: x[0])
for item in count:
    print(item[0], item[1])
