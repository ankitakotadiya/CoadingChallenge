'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,2,3]
'''

'''
# For iterative will use stack.
# Initially push root of tree to the stack.
# Run through loop until stack is non empty.
# Each and evry iteration pop top of the element from the stack and append it to our result.
# Simultaneously, push first right node and then left node into stack if they are not null. So at the top of the stack we have left node.
# Follow same process till stack is non-empty.
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack =[]
        
        if not root:
            return []
        stack.append(root)
            
        
        res = []
        
        while len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
        return res
