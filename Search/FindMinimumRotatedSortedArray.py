'''
# The approach is binary search.
# Set left and right pointer at 0 and last element and find out mid point.
# If mid point is less then or equal to the last element then element lies in the left part.
# Else minimum element lies in the right part.
# Follow this process until left pointer less than equal to the right pointer and at the end return value at the left pointer which would be our answer.

Time Complexity: O(logn)
Space Complexity: O(1)
'''

'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            
            mid = (l+r)//2
            
            if nums[mid] <= nums[-1]:
                r = mid-1
            
            else:
                l = mid+1
                
        return nums[l]
