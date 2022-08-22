'''
# The array is sorted so simply product of last three number is our answer.
# We need to check that that is last three values are negative then would get negative product, in such case will check if product of first three values are greater than the last three then return product of first three.
# Else would return product of last three values.

Time Complexity: O(1)
Space Complexity: O(1)
'''

'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Input: nums = [1,2,3,4]
Output: 24
'''

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
