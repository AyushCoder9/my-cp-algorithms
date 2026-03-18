def maxSubArraySum(nums):
    if not nums:
        return 0

    max_so_far = nums[0]
    current_max = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)

    return max_so_far

input_array_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum subarray sum for {input_array_1}: {maxSubArraySum(input_array_1)}")

