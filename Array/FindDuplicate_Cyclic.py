'''
# In the ccyclic sort, element = index+1 that means at index 0 value would be 1.
# Will run the loop until last element or found duplicate element.
# Will findout j from value at index i minus 1. 
# Now check arr[i] != arr[j] then simply swap value at i and value at j. So at i index right element has been placed.
# If arr[i] == arr[j] but index i != value at index - 1 so that element is duplicate return that element and break the loop.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        
        while i < len(nums):
            j = nums[i] - 1
            
            if nums[i] != nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
            
            elif nums[i] == nums[j] and i != nums[i] - 1:
                return nums[i]
            else:
                i+=1
