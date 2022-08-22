'''
# The approach is binary search.
# Let's assume that two array A and B with A having minimum number of elements. If this is not the case then we swap A and B to make A smaller.
# Let n be the size of A and m be the size of B.
# Actual medial of both array A and B will be n+m+1/2.
# Find mid point of array A also simultaneously split array B by substracting mid point of A from actual mid point of merged array.
# Now we have four variable.
  - leftA which is rightmost element in the left part of A. Placed at mid-1.
  - leftB which is rightmost element in the left part of B. Pleaced at mid-1.
  - rightA which is leftmost element in the right part of A. Mid point.
  - rightB which is leftmost element in the right part of B. Mid point.
  
# Hence to confirm that partition was correct or not, so will check if leftA <= rightA and leftB <= rightA then partition are correct.
# If condition fails and we found leftA > rightA then need to find another mid point of array A so will simply discard right part of array A so would have smaller mid point.
# If we found leftB > rightA then we simply discard left part of array A so will get smaller mid point of array B.
# Afterwards, if we get the correct partition then will check two conditions to return median.
  If total size of merged array is even then simply will add max(leftA,leftB) and min(righA,righB) divide by 2.
  Else will just return maximum of leftA and leftB.
  
Time Complexity: O(min(logm.logn))
Space Complexity: O(1)
'''

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            
        n = len(nums1)
        m = len(nums2)
        if (n > m):
            return self.findMedianSortedArrays(nums2, nums1)  # Swapping to make A smaller
  
        start = 0
        end = n
        realmidinmergedarray = (n + m + 1) // 2
  
        while (start <= end):
            mid = (start + end) // 2
            print(mid)
            leftAsize = mid
            leftBsize = realmidinmergedarray - mid
            
            print('L R',leftAsize,leftBsize)
              
            # checking overflow of indices
            leftA = nums1[leftAsize - 1] if (leftAsize > 0) else float('-inf')
            leftB = nums2[leftBsize - 1] if (leftBsize > 0) else float('-inf')
            rightA = nums1[leftAsize] if (leftAsize < n) else float('inf')
            rightB = nums2[leftBsize] if (leftBsize < m) else float('inf')
  
            # if correct partition is done
            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                return max(leftA, leftB)
  
            elif (leftA > rightB):
                end = mid - 1
            else:
                start = mid + 1
