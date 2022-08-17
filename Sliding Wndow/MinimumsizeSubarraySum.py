class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        start = 0
        end = 0
        minlength = float('inf')
        sumval = 0
        
        while end <= len(nums):
            
            if sumval < target:
                
                if end < len(nums):
                    sumval+=nums[end]
                    end+=1
                else:
                    end+=1
            
            else:
                minlength = min(end-start,minlength)
                print(minlength)
                sumval-=nums[start]
                print(sumval)
                start+=1
        
        if minlength == float('inf') :
            return 0
        
        return minlength
