'''
# The approach is binary search.
# First of all will set left and right pointer at 0 index and last index, using left and right pointer will find mid element.
# If mid value is greater than the just before element placed and less then the next element then will return mid value because this is the first occerence element.
# Here will discard left part in two case.
  - When mid element is even and equal to the mid+1 element that means our element is not present in left part because all the elements are twice.
  - When mid element is odd and equal to the mid-1 that means our element is not present in the left part will search in the right part.
  
# Otherwise will discard left part.

Time Complexity: O(logn)
Space Complexity: O(1)
'''

'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[l] != nums[l+1]:
            return nums[l]
        
        if nums[r] != nums[r-1]:
            return nums[r]
        
        while l <= r:
            
            mid = (l + r)//2
            print(mid)
            
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            elif (nums[mid] == nums[mid + 1] and mid % 2 == 0) or (nums[mid] == nums[mid - 1] and mid % 2 != 0):
                l = mid+1
                
            else:
                r = mid-1
