# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Approach: Sliding window (track min price and max profit)
# Difficulty: Easy
# Date: July 12, 2025

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')   
        max_profit = 0           

        for price in prices:
            if price < min_price:
                min_price = price  
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit  

        return max_profit


feat: solved 'Best Time to Buy and Sell Stock' using sliding window!

