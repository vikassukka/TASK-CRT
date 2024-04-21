def max_profit(prices):
    if len(prices) < 2:
        return 0

    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit

# Example usage:
prices = [5, 8, 11, 9, 7]
print(max_profit(prices))
