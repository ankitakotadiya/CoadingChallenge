class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1
        maxp = 0
        
        while r < len(prices):
            
            if prices[l] < prices[r]:
                maxp+=(prices[r]-prices[l])
            
            l+=1
            r+=1
            
        return maxp
