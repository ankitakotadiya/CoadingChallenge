class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        s = 0
        start = 0
        
        for i in range(len(nums)):
            
            
            if s == k:
                return len(nums[start:i])
            elif s > k:
                s-=nums[start]
                start+=1
                s+=nums[i]
            else:
                s+=nums[i]
        
        if s != k:
            return -1
        return len(nums[start:i+1])
