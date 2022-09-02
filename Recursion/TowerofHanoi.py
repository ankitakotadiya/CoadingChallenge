'''
Write a program which prints a sequence of operations that transfers n rings from one peg to another. You have a third peg, which is initially empty. The only operation you can perform is taking a single ring from the top of one peg and placing it on the top of another peg. You must never place a larger ring above a smaller ring.
'''

'''
# This problem can be solved by recursion.
# First will shift n-1 rings to peg B with help of peg C.
# Largest ring to destination peg C and shift n-1 ring to destination peg C with help of A.

Time complexity: O(2^n)
Space Complexity: O(n)
'''

class Solution:
  
  result = []
  def hanoi(self,n,source,dest,aux):
    
    self.hanoi(source,aux,dest)
    self.result.append((source,dest))
    self.hanoi(aux,dest,source)
    
  
obj = Solution()
obj.hanoi(4,0,2,1)
