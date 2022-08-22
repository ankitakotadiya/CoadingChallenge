'''
# This problem can be solved using two pointer.
# Set left pointer at 0 index and right pointer at index 1.
# If right value is greater than the left value then calculate profit by substracting right value from left.
# Initially our max_profit was 0 so update profit to max_profit variable.
# Here, will not move left pointer because it already has smaller value than right so will move right pointer by one again check the profit if profit is greater than previous store then will update to max_profit variable.
# Continue move right pointer until find any smaller value than left in such case there is no profit will set left pointer equal to the right pointer and increase right pointer by one.
# Follow the same steps at the end of loop and return maximum profit.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1
        maxp = 0
        
        while r <= len(prices)-1:
            
            if prices[l] < prices[r]:
                maxp = max(prices[r]-prices[l],maxp)
                r+=1
            
            else:
                l=r
                r+=1
                
        return maxp
