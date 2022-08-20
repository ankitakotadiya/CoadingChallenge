'''
# First of all run through loop of first array and store element and its frequency to hash map.
# Iterate each elements in second array check one by one if element exists in hash map then simply append into out result and decrease count of that element from hash map. So same element comes next time we could append in our result if count of that element in hash map greater than 0.

Time Complexity: O(n+m) n and m are length of both the arrays.
Space Complexity: O(1)
'''
'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        counts = {}
        res = []
        
        for num in nums1:
            
            counts[num] = counts.get(num,0)+1
            
        for num in nums2:
            
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1
                
        return res
