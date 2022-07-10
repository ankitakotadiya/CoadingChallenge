class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxdis = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            
            maxdis = max(min(height[left],height[right]) * (right-left),maxdis)
            
            if height[left] <= height[right]:
                left+=1
            
            else:
                right-=1
                
        return maxdis
