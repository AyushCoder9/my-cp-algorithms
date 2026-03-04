def reverse_part(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate_inplace(nums, k):
    n = len(nums)
    if n <= 1:
        return
    k %= n
    if k == 0:
        return

    reverse_part(nums, 0, n - 1)
    reverse_part(nums, 0, k - 1)
    reverse_part(nums, k, n - 1)

nums_inplace = [1, 2, 3, 4, 5, 6, 7]
k_steps = 3
rotate_inplace(nums_inplace, k_steps)
print(f"In-place right rotation by {k_steps}: {nums_inplace}")
