'''
# In this problem rotate last kth element.
# We run the loop from 0 to kth element and each and every iteration pop element from array insert at 0 index.
# At the end of loop you would get rotated array

Time Complexity: O(k)
Space Complexity: O(1)
'''

'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

nput: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        l = 0
        
        while l < k:
            
            lastval = nums.pop(-1)
            nums.insert(0,lastval)
            l+=1
