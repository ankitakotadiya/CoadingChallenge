'''
# The idea is to get total sum of array first.
# Initilise left_sum as 0.
# Then iterate through element and keep updating left_sum. In the loop we can right_sum by substracting an element from total sum.
# At one point if we found left_sum equal to the right_sum then simply return that index is our answe.
# Else at the end of the loop return -1.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left = 0
        total = 0
        
        for i in nums:
            total += i
            
        
        for i in range(len(nums)):
            
            total = total - nums[i]
            
            if left == total:
                return i
            
            left = left+nums[i]
            
        return -1
