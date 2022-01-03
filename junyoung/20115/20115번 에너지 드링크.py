# https://www.acmicpc.net/problem/20115

N = int(input())
n = input()
x = n.split(' ')
drink_list = []
for i in range(len(x)):
    x_i = int(x[i])
    drink_list.append(x_i)
drink_list.sort()
len = len(drink_list)
drink_max = drink_list[len-1]
for i in range(len-1):
    drink_max += drink_list[i] /2
    
print(drink_max)
