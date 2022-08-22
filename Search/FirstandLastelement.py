'''
# The approarch is binary search, which searches for a target element in given array and return index of it's first occurence in the list.
# Binary search steps as followed:
  - set left and right pointer at index 0 and last element.
  - Calculate the mid point from left and right pointer.
  - Return mid point if mid point is equal to the target value.
  - If mid value is greater then the target element then simply discard right part because array is sorted so our target element would be somewhere in the left part.
  - Same as if mid value is less than the target then discard left part.
  - So at the end serarch function would return either mid pointer if first occurence of target element is found otherwise -1.
  
# Now we have string point of the target.
# Run the loop from starting point to the length of an array and increase count until we find last occurence.
# Return first and last element.

Time Complexity: O(logn)
Space Complexity: O(1)
'''

'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search():
            l = 0
            r = len(nums) - 1
            midval = -1
            while l <= r:

                mid = (l+r)//2
                
                if nums[mid] == target:
                    
                    midval = mid
                    r = mid-1

                elif nums[mid] > target:
                    r = mid-1

                else:
                    l = mid+1
                    
            return midval

        if len(nums) > 0:
            midval = binary_search()
            if midval == -1:
                return [-1,-1]
            else:
                nextval = midval-1
                print(nextval)
                # temp = nums[midval]
                for i in range(midval,len(nums)):

                    if nums[i] == target:
                        nextval+=1

                    else:
                        return [midval,nextval]
                return [midval,nextval]
        else:
            return [-1,-1]
