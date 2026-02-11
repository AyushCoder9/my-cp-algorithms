def prefix_sum_loop(arr):
    n = len(arr)
    prefix_sums = [0] * n
    if not arr:
        return []

    prefix_sums[0] = arr[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i]
    return prefix_sums

input_array = [10, 20, 10, 5, 15]
result = prefix_sum_loop(input_array)
print(f"Original array: {input_array}")
print(f"Prefix sum array: {result}")
