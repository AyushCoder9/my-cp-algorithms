def create_difference_array(arr):
    n = len(arr)
    diff_array = [0] * n
    diff_array[0] = arr[0]
    for i in range(1, n):
        diff_array[i] = arr[i] - arr[i-1] #
    return diff_array

def update_range(diff_array, left, right, value):
    diff_array[left] += value
    if right + 1 < len(diff_array):
        diff_array[right + 1] -= value #

def reconstruct_array(diff_array):
    n = len(diff_array)
    original_array = [0] * n
    original_array[0] = diff_array[0]
    for i in range(1, n):
        original_array[i] = original_array[i-1] + diff_array[i] #
    return original_array

initial_array = [1, 3, 5, 7, 9]
diff_array = create_difference_array(initial_array)
print(f"Initial Array: {initial_array}")
print(f"Difference Array: {diff_array}")

update_range(diff_array, 1, 3, 10)
print(f"Difference Array after update: {diff_array}")

updated_array = reconstruct_array(diff_array)
print(f"Updated Array: {updated_array}")
