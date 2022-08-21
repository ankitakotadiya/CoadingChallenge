'''
# The approach is binary search. 
# We will set left pointer at zero position and right pointer at last position of an array.
# Using left and right pointer calculate the mid value.
# Now our array is divided into two equal partition. 
# Now we need to check that whether left part is sorted or right part. 
# If rotation happened in right half part, then obviously mid value is greater than the element at left index that means left part is sorted we need to look our target value somewhere in right part.
# If element at left is less than equal to the target and mid element is greater than target then will discard right part otherwise discard left part.
# Follow the reverse process if mid value is smaller than the left element, that means right part is sorted and our element would be placed somewhere in the left part.
# If mid value and element placed at left pointer both are equal then simply step over and increase left pointer by one.
# If mid value equal to the target then return True otherwise run the until left pointer equal to the right pointer and at the end return False.

Time Complexity: O(logn)
Space Complexity: O(1)
'''

'''
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = len(nums)
        l = 0
        r = n-1
        
        while l <= r:
            
            mid = (l + r)//2
            
            if nums[mid] == target:
                return True
            
            elif nums[mid] > nums[l]:
                                    
                if nums[l] <= target and nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
                
            elif nums[mid] < nums[l]:
                
                if  nums[r] >= target and nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
                
            else:
                l+=1
                    
            
        return False
