def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1): #거꾸로
            if arr[j] < arr[j-1]: #나보다 더 큰놈이 앞에 있으면:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
insertion_sort(arr)
print(arr)