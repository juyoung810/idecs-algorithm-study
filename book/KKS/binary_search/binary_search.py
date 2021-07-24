def binary_sort(sortedlist, target):
    low = 0
    high = len(sortedlist) - 1

    while low <= high:
        guess = (low + high) // 2
        if sortedlist[guess] == target:
            return guess
        if sortedlist[guess] < target: # 예측값이 타겟보다 작을때
            low = guess + 1
        else: # 예측값이 타겟보다 클때
            high = guess - 1
    return None