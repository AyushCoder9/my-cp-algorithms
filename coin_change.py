#question
"""Finds the fewest number of coins needed to make up a given amount"""

import math

def coinChange(coins, amount):
    memo = {}

    def dfs(remaining_amount):
        if remaining_amount == 0:
            return 0  
        if remaining_amount < 0:
            return float('inf') 

        if remaining_amount in memo:
            return memo[remaining_amount]

        min_coins = float('inf')
        for coin in coins:
            result = dfs(remaining_amount - coin)
            if result != float('inf'):
                min_coins = min(min_coins, 1 + result)

        memo[remaining_amount] = min_coins
        return min_coins

    result = dfs(amount)

    return result if result != float('inf') else -1

coins = [1, 2, 5]
amount = 11
print(f"Minimum coins needed for {amount} with coins {coins}: {coinChange(coins, amount)}")

coins2 = [2]
amount2 = 3
print(f"Minimum coins needed for {amount2} with coins {coins2}: {coinChange(coins2, amount2)}")
