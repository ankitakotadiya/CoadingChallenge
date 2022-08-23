'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
'''

'''
# We run the loop from 0 to length of the main array.
# Initially will store first elemrnt at top of stack because initially we have an empty stack.
# When it comes to the second element, check current element is greater than last element stored in stack or not, if yes then save current element as key and greater element as value.
# Will remove last element from the stack as element has been saved in hash map and save current element at top of stack.
# will keep saving smaller elements at the top of stack until find next greater once found will set greater value in hash map.
# Once this iteration is done will run loop of sub array.
# For each and every element will search in hash if any greater element presents for that particular current element then will set greater element at current position otherwise -1.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        diff = {}
        
        for pos, val in enumerate(nums2):
            
            while stack and val > stack[-1]:
                diff[stack.pop()] = val
            
            stack.append(val)
        for pos in range(len(nums1)):
            
            if nums1[pos] in diff:
                nums1[pos] = diff[nums1[pos]]
            else:
                nums1[pos] = -1
        
        return nums1

