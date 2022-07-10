class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i,data in enumerate(nums):
            
            b = target - data
            
            if b in nums:
                
                j = nums.index(b)
                
                if i == j:
                    continue
                return [i,j]
