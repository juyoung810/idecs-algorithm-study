import sys
input = sys.stdin.readline
import math

def get_height(x, y, w):
    h1 = math.sqrt(x**2-w**2)
    h2 = math.sqrt(y**2-w**2)
    h = h1*h2/(h1+h2)
    return h

x, y, c = map(float, input().split())
w_s = 0
w_e = min(x, y)
dif = 1
res_w = 0

while (w_e - w_s) >= 10**(-6) :
    mid = (w_s+w_e)/2
    h = get_height(x, y, mid)
    if h >= c :
        w_s = mid
    else:
        w_e = mid
    res_w = mid
print(res_w)

#######################################
import sys
input = sys.stdin.readline
import math

def get_height(x, y, w):
    h1 = math.sqrt(x**2-w**2)
    h2 = math.sqrt(y**2-w**2)
    h = h1*h2/(h1+h2)
    return h

x, y, c = map(float, input().split())
w_s = 0
w_e = min(x, y)
dif = 1
res_w = 0
while True :
    mid = (w_s+w_e)/2
    h = get_height(x, y, mid)
    dif = abs(c-h)
    if dif > 10**(-6):
        if c >= h:
            w_e = mid
        else:
            w_s = mid
    else:
        res_w = mid
        break
        
print(res_w)


#######################################
# https://jinho-study.tistory.com/687

# def f(x, y, w):
#     h1 = (x**2-w**2)**0.5
#     h2 = (y**2-w**2)**0.5    
#     c = h1*h2 / (h1+h2)
#     return c
    
# x, y, c = map(float, input().split())
# s, e = 0, min(x, y)
# res = 0
# while e-s > 0.000001:
#     m = (s+e)/2
#     if f(x, y, m) >= c:
#         res = m
#         s = m
#     else:
#         e = m
# print(res)