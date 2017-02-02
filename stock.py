# This answer is incorrect because the highest stock price can come before the lowest

"""
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

def get_max_profit(array):
    new_array = sorted(array)
    var_1 = new_array[0]
    var_2 = new_array[(len(new_array) - 1)]
    return (var_1 - var_2)


get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
"""

# will update the prices as it iterates through taking O(n) time with O(1) space
def get_max_profit(prices):
    if len(prices) < 2:
        return "need at least 2 prices"
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    for index, current_price in enumerate(prices):
        if index == 0:
            continue
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price  = min(min_price, current_price)
    return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
get_max_profit(stock_prices_yesterday)
