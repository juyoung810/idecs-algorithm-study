import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()

def finding_left(a,b,dots):
    #a보다 크거나 같은 가장작은 원소의 인덱스
    if a <= dots[0]: #선분의 시작지점이 가장 작은 원소보다 왼쪽이면
        return 0 #시작 인덱스는 0임
    else: #이진탐색
        start = 0 #인덱스의 시작값 0
        end = len(dots)-1#인덱스의 끝값
        while start <= end:
            mid = (start + end)//2
            if a <= dots[mid] <= b: #mid인덱스에 해당하는 점이 선분에 있으면
                end = mid - 1 #가능한 점 중 가장 작은 점의 인덱스 구해야하기 때문에
            else:
                if dots[mid] < a: #mid인덱스에 해당하는 점이 선분의 시작보다 작다면
                    start = mid + 1#탐색범위의 시작포인트를 오른쪽으로 이동시킨다(키워준다)
                elif dots[mid] > b: #mid인덱스에 해당하는 점이 선분의 끝보다 크다면
                    end = mid - 1 #탐색범위의 끝 포인트를 왼쪽으로 이동시킨다(작게한다)
    return start

def finding_right(a, b, dots):
    #b보다 작거나 같은 가장 큰 원소의 인덱스
    if b >= dots[-1]:  # 선분의 시작지점이 가장 작은 원소보다 오른쪽이면
        return len(dots)-1  # 마지막 인덱스 return
    else:
        start = 0
        end = len(dots) - 1
        while start <= end:
            mid = (start + end) // 2
            if a <= dots[mid] <= b:
                start = mid + 1
            else:
                if dots[mid] < a:
                    start = mid + 1
                elif dots[mid] > b:
                    end = mid - 1
    return end

for i in range(M):
    a, b = map(int,input().split())
    left_idx = finding_left(a,b, dots)
    right_idx = finding_right(a,b, dots)
    print(right_idx- left_idx + 1)