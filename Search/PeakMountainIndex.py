'''
# The approach is binary search.
# First partition array in two equal parts and find the mid element.
# Noew check if ellement placed just before and after mid is less than the mid element than mid element is our answer.
# if element placed before mid is less than the mid but after is greater than mid then discard right part because peak element placed in left part only.
# If not the case and left element is greater than mid the discard left part your peak element is in right part.
# Partition the array until find peak element.

Time Complexity: O(logn)
Space Complexity: O(1)
'''

'''
Given a mountain arr return index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
Input: arr = [0,10,5,2]
Output: 1
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            
            mid = (low+high)//2
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                low = mid
            else:
                high = mid
