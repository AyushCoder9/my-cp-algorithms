#Question
'''find the maximum amount of money you can steal from a row of houses, given that you cannot rob two adjacent houses'''
def rob(nums):
    memo = {}
    def dfs(i):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        res = max(nums[i] + dfs(i + 2), dfs(i + 1))
        memo[i] = res
        return res

    return dfs(0)

print(rob([2, 7, 9, 3, 1]))
