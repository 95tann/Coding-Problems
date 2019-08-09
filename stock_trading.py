'''
Topic   : Arrays
Problem : Best Time to Buy and Sell Stocks I
Link    : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
def maxProfit(prices):
    if prices == []:
        return 0
    
    max_index, min_index, profit = 0, 0, 0
    
    for i, price in enumerate(prices):
        if price > prices[max_index]:
            max_index = i
        
        if price < prices[min_index]:
            min_index, max_index = i, i
    
        if profit < prices[max_index] - prices[min_index]:
            profit = prices[max_index] - prices[min_index]
        
    return profit


''' 
Topic   : Arrays
Problem : Best Time to Buy and Sell Stocks II
Link    : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
def maxProfit(prices):
    if prices == []:
        return 0
    
    profit = 0
    buy_index, sell_index = 0,0
    for i in range(1,len(prices)):
        if prices[i] > prices[sell_index]:
            sell_index = i
        
        if prices[i] < prices[sell_index]:
            profit += prices[sell_index]-prices[buy_index]
            buy_index, sell_index = i,i
        
    profit += prices[sell_index] - prices[buy_index]
    return profit
