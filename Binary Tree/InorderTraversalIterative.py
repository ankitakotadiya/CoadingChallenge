'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,2,3,4,5,null,null]
Output: [4,2,5,1,3]
'''

'''
# Create an empty stack.
# Initilise current node as root.
# Push the current node to the stack and set current node equal to left node.
# If current node is Null and stack is non-empty then pop item from the stack and append it to our result.
# Simultaneously update current node equal to right node of poped node.
# Follow above step if current is not null then push current node into stack.
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        stack = []
        res = []
        
        while True:
            if current is not None:
                stack.append(current)

                current = current.left
                
            elif (stack):
                current = stack.pop()
                
                res.append(current.val)
                
                current = current.right
                
            else:
                break
                
        return res
