def lengthOfLIS(nums):
    if not nums:
        return 0
    memo = {}

    def solve(i):
        if i in memo:
            return memo[i]
        
        max_len = 1
        for j in range(i):
            if nums[i] > nums[j]:
                max_len = max(max_len, solve(j) + 1)
        
        memo[i] = max_len
        return max_len

    return max(solve(i) for i in range(len(nums)))

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of LIS:", lengthOfLIS(nums))
