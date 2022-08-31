'''
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
'''

'''
# Run the loop from start to end.
# Each and every iteration will update total can be calculated by previouls element's reminder plus current element divide by k and reminder will save in total.
# Current total will check in hashmap if not exist then save key as total value as index.
# If total exist then will check diff between current index and index saved in hashmap. If it is greater than 1 then array contains multiple of k. Return true and break the loop else return false end of iteration.

Time Complexity: O(n)
Space Complexity: O(k), multiple of k.
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        total = 0
        dic = {0:-1}
        
        for i in range(len(nums)):
            
            total = (total + nums[i]) % k
            print(total)
            if total not in dic:
                dic[total] = i
            
            elif i - dic[total] >= 2:
                return True
            
                
        return False
