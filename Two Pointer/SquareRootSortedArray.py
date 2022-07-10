class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l = 0
        r = len(nums) - 1
        
        if len(nums) == 1:
            return [nums[0] * nums[0]]
        
        while l < r:
            
            if abs(nums[l]) >= abs(nums[r]):
                
                nums[l] = nums[l] * nums[l]
                temp = nums[l]
                nums.pop(0)
                nums.insert(r,temp)
                r-=1
                
                if r == 0:
                    nums[r] = nums[r]*nums[r]
                
            else:
                
                nums[r] = nums[r] * nums[r]
                r-=1
                
                if l == r:
                    nums[l] = nums[l] * nums[l]
                
            
        return nums
