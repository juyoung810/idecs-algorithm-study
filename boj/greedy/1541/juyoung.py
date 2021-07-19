import sys
eq = sys.stdin.readline().rstrip('\n').split('-')
#print(eq)

for i in range(len(eq)):
    eq_num = list(map(int,(eq[i].split("+"))))
    eq[i] = sum(eq_num)

result = eq[0]
for i in range(1,len(eq)):
    result -= eq[i]

sys.stdout.write(str(result))
