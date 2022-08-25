'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,2,3], k = 3
Output: 2
'''

'''
# Initilise hashmap key as 0 and it's value equal to 1.
# Traverse the array and store sum of the each element in prevsum.
# Also maintain the count of different value of prevsum in hashmao.
# Now check in hashmap number of subarray previousy found having sum = prevsum - targetsum(k).
# If yes then get the count and add with our subarray count.
# If not then save prevsum against count 1 if not exists else increase count for current presum.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        presum = 0
        d = {0:1}
        
        for num in nums:
            
            presum += num
            
            if presum - k in d:
                ans = ans + d[presum-k]
                
            if presum not in d:
                d[presum] = 1
                
            else:
                d[presum] = d[presum] + 1
                
        return ans
