'''
# Traverse the array from right to left and find out first element who is not following ascending order. Let's say 12543 then 2 is not following ascending order.
# If you reach at 0 index and all the elements are following ascending order then simply reverse the array and return result.
# Consider that element as pivot and swap with smallest element on right side.
# After swapping with pivoit, set all the element after pivot in ascending order, which is our next permutation.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].

Input: nums = [1,2,3]
Output: [1,3,2]
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        i = len(nums) - 1
        
        if len(nums) == 1:
            return 
        
        while i > 0 and nums[i-1] >= nums[i]:
            i-=1
            
        if i == 0:
            nums.reverse()
            return
        
        piv = i - 1
        j = len(nums) - 1
        
        while j>=0 and nums[j] <= nums[piv]:
            j-=1
            
        nums[j],nums[piv] = nums[piv],nums[j]
        
        l = piv+1
        r = len(nums) - 1
        
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
