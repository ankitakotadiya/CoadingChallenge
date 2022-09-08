'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
'''

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def fib(self, n: int) -> int:
        
        if n <=1 :
            return n
        
        a,b = 0,1
        for _ in range(1,n):
            
            a,b = b,a+b
            print(a,b)
            
        return b
