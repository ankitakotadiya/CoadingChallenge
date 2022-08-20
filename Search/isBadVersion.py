'''
# The approach is binary search. Here will start from the l = 1 because no index operation is involved and product version starts from 1.
# First findout mid point. Here left part keep track of all good versions from start to mid and right part keep track of all bad versions from mid to end.
# Check at the mid point bad version starts or not and just before mid good version or not. If yes, then simply return mid, it is our first bad version.
# If not, then check at mid point bad version is not found discard left part by setting l = mid+1 because it has all good version.
# If you have found bad version at mid point then simply discrad right part by setting r = mid-1.
# Continue this process until you are done with first bad version.

Time Complexity: O(logn)
Space Complexity: O(1)

'''

'''
Find first bad version starts.Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

'''


def isBadVersion(version: int) -> bool:
    
    taget = 4
    
    if target == version:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l = 1
        r = n
        
        while l <= r:
            
            mid  = (l+r)//2
            
            if isBadVersion(mid) and not isBadVersion(mid-1):
                
                return mid
            
            elif not isBadVersion(mid):
                l = mid+1
            else:
                r = mid-1
