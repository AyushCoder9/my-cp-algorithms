def knapsack_memo(capacity, weights, values, n, memo):
    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    if weights[n-1] > capacity:
        memo[n][capacity] = knapsack_memo(capacity, weights, values, n-1, memo)
        return memo[n][capacity]

    else:
        include_item = values[n-1] + knapsack_memo(capacity - weights[n-1], weights, values, n-1, memo)
        exclude_item = knapsack_memo(capacity, weights, values, n-1, memo)
        memo[n][capacity] = max(include_item, exclude_item)
        return memo[n][capacity]


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)

memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

max_value = knapsack_memo(capacity, weights, values, n, memo)

print(f"Maximum value in Knapsack = {max_value}")
