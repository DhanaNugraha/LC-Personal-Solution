prices = [7,1,5,3,6,4]

def maxProfit(prices):
    left, right = 0, 0 
    output = 0

    while right < len(prices):
        profit = prices[right] - prices[left]
        output = max(profit, output)

        if profit >= 0:
            right += 1

        else:
            left += 1
    
    return output
    
print(maxProfit(prices))