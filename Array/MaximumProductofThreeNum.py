class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0]*nums[1]
        else:
            max1 = nums[0]*nums[1]*nums[-1]
            max2 = nums[-1]*nums[-2]*nums[-3]
            
            if max1 > max2:
                return max1
            else:
                return max2
