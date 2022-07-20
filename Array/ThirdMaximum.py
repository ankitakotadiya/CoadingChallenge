class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
            
        else:
            
            count = 1
            for i in range(n):
                
                for j in range(0,n-i-1):
                    
                    if nums[j] > nums[j+1]:
                        nums[j],nums[j+1] = nums[j+1],nums[j]
                        
                if  i > 0 and nums[n-i] > nums[n-i-1]:
                    count+=1
                
                if count == 3:
                    return nums[n-i-1]
                
                    
        return nums[-1]
