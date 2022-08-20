'''
# The approach is binary search. 
# Set left point equal to 0 and right pointer qual to x.
# Find out mid point and calculate square of mid point.
# If square of mid point is equal to the given number then return mid is the our answer.
# If squre is greater than x then discard right part because square should not be greater than num so we need to search in left part only.
# If less than then discard left part and will continue searach in right part until we find square root.

Time Complexity: O(logn)
Space Complexity: O(1)
'''

'''
Given a non-negative integer x, compute and return the square root of x.

Input: x = 4
Output: 2
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        
        s = 0
        e = x
        
        while s <= e:
            
            mid = (s+e)//2
            
            mul = mid*mid
            
            if mul == x:
                return mid
            elif mul < x:
                s = mid+1
            else:
                e = mid-1
                
        return e
