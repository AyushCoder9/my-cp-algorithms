def partition_array(arr, low, high):
    pivot = arr[high]
    i = low - 1  

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [10, 7, 8, 9, 1, 5]
low = 0
high = len(arr) - 1
partition_index = partition_array(arr, low, high)
print("Partitioned array:", arr)
print("Pivot index:", partition_index)
