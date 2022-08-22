'''
# Create three variable first_max, second_max, third_max to store first, second and third largest element.
# Initially set first_max value at 0 index and minimum value to second_max and third_max.
# Traverse the array, each and every iteration check current element is larger than first_max or not, update the first_max, if element is larger. Also assign first_max to second_max and second_max to third_max.
# So the previously stored largest value become second largest and second largest become third largest.
# Else if current element is larger than the second_max then update the value of second and second largest become third largest.
# If previous two conditions fail, but the current element is larger than third_max then update third_max.
# At the end of the loop return third_max if it has not minimum value else return first_max.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        max1 = nums[0]
        secmax = float('-inf')
        thimax = float('-inf')
        
        if len(nums) < 3:
            return max(nums)
        
        for num in nums:
            
            if num > max1:
                thimax = secmax
                secmax = max1
                max1 = num
                
            elif num > secmax and num < max1:
                thimax = secmax
                secmax = num
                
            elif num > thimax and num < secmax:
                thimax = num
                
        return thimax if thimax != float(-inf) else max1
