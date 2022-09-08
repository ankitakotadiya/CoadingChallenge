'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''

'''
Time Complexity: O(n-3)
Space Complexity: O(1)
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 3:
            return n
        
        a,b = 2,3
        for _ in range(3,n):
            
            a,b = b,a+b
            
        return b
