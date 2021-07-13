def gcd(a, b):
    if b != 0: return gcd(b,a%b)
    else: return a

a, b = map(int, input().split())

gcd_num = gcd(a, b)
lcm_num = gcd_num*(a // gcd_num) * (b // gcd_num)
print(gcd_num)
print(lcm_num)