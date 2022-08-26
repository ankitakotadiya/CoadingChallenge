'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
'''

'''
# Traverse tree in preorder fashion.
# For evry traversal check subtree is rooted with current node or not.
# If yes then return True for that node else False.

Time Complexity: O(m*n) where m and n are given nodes in both subtree.
Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False
        
        if not subRoot:
            return True
        
        if self.sameTree(root,subRoot):
            return True
        
        l = self.isSubtree(root.left,subRoot)
        r = self.isSubtree(root.right,subRoot)
        
        return l or r
    
    def sameTree(self,root,sub):
        
        if not root and not sub:
            return True
        
        if root and sub and root.val == sub.val:
            return self.sameTree(root.left,sub.left) and self.sameTree(root.right,sub.right)
