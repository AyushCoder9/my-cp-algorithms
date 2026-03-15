def longestCommonSubstring(s1, s2):
    n, m = len(s1), len(s2)
    memo = {}

    def helper(i, j):
        if i < 0 or j < 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        count = 0
        if s1[i] == s2[j]:
            count = 1 + helper(i - 1, j - 1)
        memo[(i, j)] = count
        return memo[(i, j)]

    max_len=0
    for i in range(n):
        for j in range(m):
            max_len=max(max_len, helper(i,j))
    return max_len


#Question
'''Find the length of the longest common substring between two strings s1 and s2.'''

print(longestCommonSubstring("abcdef", "abcfgh"))