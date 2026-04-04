def unbounded_knapsack_memo(weights, values, capacity):
    n = len(weights)
    memo = {}

    def solve(i, current_capacity):
        if i < 0 or current_capacity == 0:
            return 0
        
        state = (i, current_capacity)
        if state in memo:
            return memo[state]
        
        result = solve(i - 1, current_capacity)
        
        if weights[i] <= current_capacity:
            include = values[i] + solve(i, current_capacity - weights[i])
            result = max(result, include)
            
        memo[state] = result
        return result

    return solve(n - 1, capacity)

weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8
max_value = unbounded_knapsack_memo(weights, values, capacity)
print(f"Maximum value: {max_value}") 
