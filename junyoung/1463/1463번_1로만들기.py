'''
                     1  2  3  4  5  6  ..
          -1 사용    0  1  2  3  4  5
2이나 3으로 나누기    0  1  1  
'''

import sys
input = sys.stdin.readline
x = int(input())

count = [[0 for i in range(x)] for j in range(2)]
for i in range(x):
    count[0][i] = i
for i in range(1, x):
    n = i+1
    if n %2 ==0 and n %3 ==0:
        count[1][i] = min(count[1][n//2-1], count[1][n//3-1], count[0][n//2-1], count[0][n//3-1]) +1
    elif n%2 ==0 and n%3 != 0:
        count[1][i] = min(count[1][n//2-1], count[0][n//2-1], count[1][i-1]) +1
    elif n%2 !=0 and n%3 == 0:
        count[1][i] = min(count[1][n//3-1], count[0][n//3-1], count[1][i-1]) +1
    else:
        count[1][i] = min(count[1][i-1]+1, count[1][i-2]+2)
        
x_count = count[1][x-1]
print(x_count)

# count[0]은 신경 안써도 되나????????????????????????????
# import sys
# input = sys.stdin.readline
# x = int(input())

# count = [[0 for i in range(x)] for j in range(2)]
# for i in range(x):
#     count[0][i] = i
# for i in range(1, x):
#     n = i+1
#     if n %2 ==0 and n %3 ==0:
#         count[1][i] = min(count[1][n//2-1], count[1][n//3-1]) +1
#     elif n%2 ==0 and n%3 != 0:
#         count[1][i] = min(count[1][n//2-1], count[1][i-1]) +1
#     elif n%2 !=0 and n%3 == 0:
#         count[1][i] = min(count[1][n//3-1], count[1][i-1]) +1
#     else:
#         count[1][i] = min(count[1][i-1]+1, count[1][i-2]+2)
        
# x_count = count[1][x-1]
# print(x_count)