class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left = 0
        total = 0
        
        for i in nums:
            total += i
            
        
        for i in range(len(nums)):
            
            total = total - nums[i]
            
            if left == total:
                return i
            
            left = left+nums[i]
            
        return -1
