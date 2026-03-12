#question
'''Checks if a subset of 'arr' sums to 'target_sum' using recursion with memoization.'''

def is_subset_sum_memo(arr, target_sum):
    memo = {}

    def solve(index, current_target):
        if current_target == 0:
            return True
        
        if index == len(arr) or current_target < 0:
            return False
        
        if (index, current_target) in memo:
            return memo[(index, current_target)]

        include = solve(index + 1, current_target - arr[index])
        exclude = solve(index + 1, current_target)
        result = include or exclude
        memo[(index, current_target)] = result
        return result
    return solve(0, target_sum)


numbers = [3, 34, 4, 12, 5, 2]
target = 9

if is_subset_sum_memo(numbers, target):
    print(f"Found a subset with sum {target} in the array {numbers}.")
else:
    print(f"No subset with sum {target} found in the array {numbers}.")

target = 30
if is_subset_sum_memo(numbers, target):
    print(f"Found a subset with sum {target} in the array {numbers}.")
else:
    print(f"No subset with sum {target} found in the array {numbers}.")
