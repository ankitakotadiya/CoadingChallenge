'''
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
'''

'''
# Create a\one empty stack and push root node in it.
# Run through loop until stack is non-empty.
# Each and every iteration initilise count = 0 each levels elements will store in list ele = [], and length of the stack.
# Run one inner loop till count less than length of the stack.
# Keep popping item from the stack and insert their children into stack. Simultaneously append that popoed item's value in ele array.
# Once count equal to length of stack that means one level has been finished so end of this inner loop append ele array to the result.
# Follow same process by initilising count,length of stack and ele array.
# At the end return result.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        stack = []
        level = []
        stack.append(root)
        
        while(len(stack) > 0):
            
            count = 0
            l = len(stack)
            ele = []
            
            while count < l:
                count += 1
                node = stack.pop()
                
                ele.append(node.val)
                
                if node.left is not None:
                    stack.insert(0,node.left)
                    
                if node.right is not None:
                    stack.insert(0,node.right)
                    
            level.append(ele)
            
        return level[::-1]
