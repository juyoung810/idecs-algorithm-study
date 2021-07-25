def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i ,end = ' ')

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
counting_sort(array)