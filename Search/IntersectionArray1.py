'''
# The approach is binary search.
# Sort first array and run througn loop of second array.
# Iterate one by one element and search an element first array using binary search. Steps as followed below
  - First find out mid point.
  - If element placed at mid then simply return true.
  - If element at mid is greater than target element then discard right part because out element would be placed somewhere in left part.
  - If mid element is smaller then discard left part.
  - If not found then return False.
  
# If element found using binary search then store that element in hash map.
# Follow the process to the end of iteration and return all keys of hash map which would our answer.

Time Complexity: O(nLogn)
Space Complexity: O(1)
  
'''

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def binary_search(b,n,k):
            
            l = 0
            r = n-1
            
            while l <= r:
                
                mid  = (l+r)//2
                
                # print(mid)
                if b[mid] == k:
                    return True
                
                elif b[mid] > k:
                    r = mid-1
                
                else:
                    l = mid+1
            return False
        
        hmap = {}
        nums1.sort()
        
        for i in nums2:
            if binary_search(nums1,len(nums1),i):
                hmap[i] = 1
        return hmap.keys()
