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
