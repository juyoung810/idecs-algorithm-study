def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        guess = (low + high) // 2
        if sorted_list[guess] == target:
            return guess
        if sorted_list[guess] < target:
            low = guess + 1
        else:
            high = guess - 1
    return None


n = int(input())
arr1 =list(map(int,input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int,input().split()))

for item in arr2:
    result = binary_search(arr1, item)
    if result == None:
        print('no', end = ' ')
    else:
        print('yes', end = ' ' )