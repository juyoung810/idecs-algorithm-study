from itertools import combinations
def solution(n, weak, dist):
    # n 포인트 갯수/ weak 취약점 위치 / dist 친구들별로 움질일 수 있는 거리
    # 포인트 별로 거리를 구해서 저장해야한다
    # -> 거리를 구할 큰수에서 작은수의 취약점으로 이동할때는 n - abs(x1 - x2) / 작은수에서 큰수로 갈때는 abs(x1 - x2)
    # 이동거리가 큰 친구부터 가장 긴 거리에 투입해보자
    dist_weak = []
    for i in range(len(weak)-1):
        if weak[i+1] - weak[i] < n - (weak[i+1] - weak[i]):
            dist_weak.append((weak[i], weak[i+1], weak[i+1] - weak[i]))
        else:
            dist_weak.append((weak[i+1], weak[i], n - (weak[i+1] - weak[i])))
    dist_weak.append((weak[-1], weak[0], n - (weak[-1] - weak[0])))

    min_path = [0]
    global_min = int(1e9)

    for i in range(1,len(weak)):
        comb = combinations(dist_weak, i)
        for c in comb:
            local_min = 0
            visited = set()
            for i in range(0,len(c)):
                start, end, d = c[i]
                visited.add(start)
                visited.add(end)
                local_min += d
            if len(visited) == len(weak):
                if global_min > local_min:
                    global_min = local_min
                    min_path.pop()
                    min_path.append(c)


    print(global_min, min_path)
    answer = 0
    return answer
solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
