class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        res = 0
        queue = []
        
        for r,num in enumerate(nums):
            
            if num == 0:
                queue.append(r)
            
            if len(queue) > k:
                indx = queue.pop(0)
                l = indx+1
            
            res = max(res,r-l+1)
        
        return res
