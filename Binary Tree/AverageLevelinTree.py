'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
'''

'''
# The idea is to create one stack and start pushing root node in it.
# Run through loop until stack is non-empthy.
# each every iteration maintain sum, count and length of the stack for each level. Initilally sum and count set to zero.
# Run one inner loop till count less than length of the stack.
# keep popping item from the stack and insert their children into stack till count less than length of stack simultaneouslu update count and sum.
# Once count equal to the length of stack that means that level is finished so append sum to the result. 
# Now again initilise sum,count = 0 and length of the stack that is all children of next level.
# Follow above steps popping item and insert their children into stack.
# At the end return result

Time Complexity: O(n)
Space Complexity: O(n)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        
        if not root:
            return
        
        stack = []
        ave = []
        stack.append(root)
        while len(stack) > 0:
            
            total = 0
            count = 0
            l = len(stack)
            
            while count < l:
                count+=1
                node = stack.pop()
                total += node.val
                
                if node.left is not None:
                    stack.insert(0,node.left)
                    
                if node.right is not None:
                    stack.insert(0,node.right)
                    
            ave.append(total/count)
            
        return ave

