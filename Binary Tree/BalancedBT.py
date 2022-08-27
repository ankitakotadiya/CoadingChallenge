'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Input: root = [3,9,20,null,null,15,7]
Output: true
'''

'''
# The approach is DFS.
# Recersively traverse left and right children.
# For every root node calculate height of left and right sub tree.
# If absolute difference between left and right subtree is less than or equal to 1 that means tree is balanced.
# At the end return True if it is blanaced else return false.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root,h=1):
            
            if not root:
                return h
            
            l = dfs(root.left,h+1)
            r = dfs(root.right,h+1)
            
            return abs(l-r) <= 1 and max(l,r)
            
        return dfs(root)
