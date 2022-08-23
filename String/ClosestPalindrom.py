'''
# If a number is single digit then simply return num-1.
# If num is 10 or 11 then return 9.
# Find out first half of given number.
# Append mirror image of firsthalf - 1, firsthalf and firsthalf + 1 at the end of it.
# Return the number whose difference to the given number is minimum.
# Here we need to handle some special case as well.
# If number contain's all 9's then we can get closest palindrom by simply adding num+2.
# If num is 1000 so will get three numbers 99,1001,1111 in such case we can find closest palindrom (a number whose length + 2 equal to the given number length)*10 + 2.

Time Complexity: O(d), number of digits.
Space Complexity: O(1)
'''

'''
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

Input: n = "123"
Output: "121"
'''

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        if int(n) < 10:
            return str(int(n) - 1)
        
        if int(n) <= 11:
            return '9'
        
        mid = len(n) // 2
        halfnum = int(n[:-mid])
        # print('mid and half',mid,halfnum)

        nums = [0] * 3
        
        for i in [-1, 0, 1]:
            nums[i+1] = str(halfnum + i)
            nums[i+1] += nums[i+1][:mid][::-1]
            nums[i+1] = int(nums[i+1])
        
        # cover the cases like 1000
        if len(str(nums[0])) + 2 == len(n):
            nums[0] = nums[0] * 10 + 9

        # cover the cases when diff[1] == n
        diff = [abs(num - int(n)) for num in nums]
        if diff[1] == 0:
            diff[1] = float("inf")
        
        # happy ending
        ind = diff.index(min(diff))
        return str(nums[ind])
