'''
# Create a deque to store k elements.
# Run a loop and insert first k elements in the deque. Before inserting the element, check if element at the back of deque is smaller than current element than remove back element and insert current so leftmost element in the deque is always greater element.
# Once you reach kth element then store leftmost element of the deque to resultant array and increase left window position by one.
# Remove the leftmost element from deque if it is out of current window.
# Insert next element in the deque, before inserting the element, check if element at the back of deque is smaller than current element then remove element at the back of deque until leftmost element greater than current one.
# At the end return maximum elements of the window.

Time Complexity: O(N)
Space Complexity: O(M), where M is number of maximum elements in the array
'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        result=[]
        q=[]
        left=0
        right=0
        
        while right<len(nums):
            while q and nums[q[-1]]<nums[right]:
                q.pop()
            q.append(right)
        
            print(q)
            if left>q[0]:
                q.pop(0)
                
            if (right+1)>=k:
                result.append(nums[q[0]])
                left+=1
            
            right += 1
            
        return result
