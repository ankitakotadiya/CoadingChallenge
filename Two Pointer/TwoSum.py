class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        fdic = {}
        for i,data in enumerate(nums):
            
            b = target - data
            
            if data in dic:
                
                return [dic[data],i]
            dic[b] = i
