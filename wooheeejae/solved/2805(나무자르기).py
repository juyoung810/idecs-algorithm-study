 # 기본 변수 설정
num, height = map(int, input().split())
trees = list(map(int, input().split()))
hMin, hMax = 1, max(trees)


 # 문제 풀이
def rest(H):
    R = 0
    for i in trees:
        if i - (H) > 0:
            R += i - (H)
    return R

while True:
    if hMin > hMax:
        break
    avg = (hMax + hMin) // 2
    if rest(avg) >= height:
        hMin = avg + 1
    else:
        hMax = avg - 1

print(hMax)