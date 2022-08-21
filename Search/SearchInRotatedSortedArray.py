'''
# The approach is binary search. 
# We will set left pointer at zero position and right pointer at last position of an array.
# Using left and right pointer calculate the mid value.
# Now our array is divided into two equal partition. 
# Now we need to check that whether left part is sorted or right part. 
# If rotation happened in right half part, then obviously mid value is greater than the element at left index that means left part is sorted we need to look our target value somewhere in right part.
# If element at left is less than equal to the target and mid element is greater than target then will discard right part otherwise discard left part.
# Follow the reverse process if mid value is smaller than the left element, that means right part is sorted and our element would be placed somewhere in the left part.
# If mid value equal to the target then return mid otherwise run the until left pointer equal to the right pointer and at the end return -1.

Time Complexity: O(logn)
Space Complexity: O(1)
'''

'''
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l = 0
        r = n-1
        
        while l <= r:
            
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < nums[l]:
                
                if nums[r] >= target and nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
                    
            else:
                if nums[l] <= target and nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
                    
        return -1
