def fractional_knapsack(values, weights, capacity):
    n = len(values)
    items = []
    for i in range(n):
        if weights[i] > 0:
            ratio = values[i] / weights[i]
            items.append((ratio, values[i], weights[i]))
        else:
            print(f"⚠️ Skipping item {i+1}: invalid weight ({weights[i]})")

    items.sort(key=lambda x: x[0], reverse=True)

    current_weight = 0
    total_value = 0.0

    print("\nItems taken:")
    for ratio, value, weight in items:
        if current_weight + weight <= capacity:
            current_weight += weight
            total_value += value
            print(f" ✅ Took full item (value={value}, weight={weight})")
        else:
            remaining_capacity = capacity - current_weight
            fraction = remaining_capacity / weight
            total_value += value * fraction
            current_weight += remaining_capacity
            print(f" ✅ Took {remaining_capacity}/{weight} of item (value={value}, weight={weight})")
            break

    return total_value

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50.0

max_val = fractional_knapsack(val, wt, W)
print(f"\n💰 Maximum value in knapsack = {max_val}")

