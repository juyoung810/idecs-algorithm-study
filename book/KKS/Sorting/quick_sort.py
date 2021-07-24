def quicksort(arr):
    if len(arr) < 2:
        return arr

    else:
        pivot = arr[0]
        tail = arr[1:]
        less = [x for x in tail if x <= pivot]
        greater = [x for x in tail if x > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(quicksort(arr))