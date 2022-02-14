N = int(input())
requests = list(map(int,input().split()))
budget = int(input())

def find_budget(requests, budget):
    if sum(requests) <= budget:
        return print(max(requests))
    else:
        low = 0
        high = max(requests)
        while low <= high:
            total = 0
            mid = (low + high) // 2
            for request in requests:
                if mid >= request:
                    total += request
                else:
                    total += mid
            if total > budget: #가능 지출보다 크면
                high = mid - 1
            else: #가능 지출보다 작으면
                low = mid + 1
        return print(high)

find_budget(requests, budget)


