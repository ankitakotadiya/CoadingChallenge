'''
# Create a result array and initilise it's value to 1 and a veriable prefix = 1.
# Traverse array from start to end.
# For every index i update result[i] = prefix and prefix = prefix * current element.
# At the end of the loop initilise prefix = 1 and traverse array from last to start.
# For every index of i update result[i] = result[i] * prefix and update prefix = prefix * current element.
# So basically in the fist loop result product of all left elements except self and in the second loop multiply product of right element except self.
# Return the result.

Time Complexity: O(2n)
Space Complexity: O(n)
'''

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for j in range(len(nums) - 1, -1,- 1):
            result[j] *= postfix
            postfix *= nums[j]
        
        return result
