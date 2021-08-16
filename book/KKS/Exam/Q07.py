n = input()
mid_idx = len(n)//2 - 1
front = n[:mid_idx+1]
rear = n[mid_idx+1:]
front = map(int, front)
rear = map(int, rear)
if sum(front) == sum(rear):
    print("LUCKY")
else:
    print("READY")