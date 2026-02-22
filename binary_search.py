def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1


my_list = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
search_element = 110

result = binary_search(my_list, search_element)

if result != -1:
    print(f"Element {search_element} is present at index {result}")
else:
    print(f"Element {search_element} is not present in array")
