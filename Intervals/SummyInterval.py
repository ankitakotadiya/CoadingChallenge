'''
# Create a list of string to store the result.
# Start travesing the array from 1 to length of an array.
# Compare previous and current element, if difference is equal to 1 that means element fall into same range.
# Once found difference greater than 1 then append formed range into result from 0 to i-1. And mark i as end end of range so next range would be start from the i.
# At the end of traversal return the result.

Time Complexity: O(n)
Space Complexity: O(m) where m is ranges stored in the list.

'''

'''
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        def help_foo(arr,left,right):
            
            if abs(left-right)>=1:
                return f'{arr[left]}->{arr[right]}'
            
            return f'{arr[left]}'
        
        res=[]
        left = 0
        
        if len(nums) == 1:
            return list(map(str,nums))
        
        for i in range(1,len(nums)):
            
            if abs(nums[i] - nums[i-1]) > 1:
                res.append(help_foo(nums,left,i-1))
                left = i
                
            if i == len(nums) - 1:
                res.append(help_foo(nums,left,i))
        
        return res
