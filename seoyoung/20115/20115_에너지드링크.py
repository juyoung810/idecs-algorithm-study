'''
에너지 드링크를 하나로 합쳐서 마시려고 한다. 합치는 과정
1. 임의의 서로 다른 두 에너지 드링크 고르기
2. 한쪽 에너지 드링크를 다른 쪽 에너지 드링크에 모두 붓기. 붓는 과정에서 원래 양의 절반을 흘림
3. 다 붓고 남은 빈 에너지 드링크는 버린다.
4. 에너지 드링크가 하나만 남을 때까지 반복
합쳐진 에너지 드링크의 양을 최대로 하려고 한다.

< 아이디어 >
1. 임의의 두 에너지 드링크를 어떻게 고를까.
2. 작은거를 큰거에 합친다. 작은걸 절반 버리는게 이득
3. 그냥 제일 큰 값에 나머지의 절반을 다 더한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))
drinks.sort(reverse=True)

result = drinks[0]
for i in range(1,n):
    result += drinks[i]/2
print(result)
