class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        i = len(nums) - 1
        
        if len(nums) == 1:
            return 
        
        while i > 0 and nums[i-1] >= nums[i]:
            i-=1
            
        if i == 0:
            nums.reverse()
            return
        
        piv = i - 1
        j = len(nums) - 1
        
        while j>=0 and nums[j] <= nums[piv]:
            j-=1
            
        nums[j],nums[piv] = nums[piv],nums[j]
        
        l = piv+1
        r = len(nums) - 1
        
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
