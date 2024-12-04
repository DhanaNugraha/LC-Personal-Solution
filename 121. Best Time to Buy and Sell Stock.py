prices = [7,1,5,3,6,4]

def maxProfit(prices):
    left, right = 0, 1
    output = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            output = max(profit, output)

        else:
            left = right

        right += 1
    
    return output
    
print(maxProfit(prices))