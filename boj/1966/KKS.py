class queue_item:
    def __init__(self, value):
        self.value = value
        self.target = False
result = []
test_case = int(input())
for _ in range(test_case):
    n, target_idx = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = [queue_item(i) for i in priority]
    queue[target_idx].target = True
    cnt = 0

    while True:
        if len(queue) == 1 and len(priority) == 1:
            result.append(1)
            break
        max_value = max(([queue_item.value for queue_item in queue][1:]))
        if queue[0].value < max_value:
            _temp = queue[0]
            queue.append(_temp)
            queue = queue[1:]
        else:
            cnt += 1
            _temp = queue[0]
            if _temp.target:
                result.append(cnt)
                break
            queue = queue[1:]

for item in result:
    print(item)
