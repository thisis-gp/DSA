 # selling price = selling price - buying price
 # buying price must be minimum and selling price should be maximum

def buy_sell_stocks(arr):
    buy_price = float("inf")
    max_profit = 0
    for selling_price in arr:
        if buy_price < selling_price:
            profit = selling_price - buy_price
            max_profit = max(profit, max_profit)
        else:
            buy_price = selling_price
    return max_profit

prices = [7,1,5,3,6,4]
print("The maximum profit is",buy_sell_stocks(prices))

# time complexity = O(N)
# space complexity = O(1)