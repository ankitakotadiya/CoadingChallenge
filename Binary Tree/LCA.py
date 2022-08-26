'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
'''

'''
# The idea is DFS.
# As our tree is binary search tree so left node always has lowest value than it's root and right node has greater value.
# First will check max(p,q) less than root node then will continue our search in left sub tree otherwise right search tree.
# Break the recursion call if root is None.
# return root in each call.
# So at the end will get ancestores.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # If tree is binary tree
    def findLCA(root, n1, n2):
     
    # Base Case
        if root is None:
            return None

        if root.val == n1 or root.val == n2:
            return root

        left_lca = findLCA(root.left, n1, n2)
        right_lca = findLCA(root.right, n1, n2)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca is not None else right_lca

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or not p or not q:
            return
        
        if max(p.val,q.val) < root.val:
            self.lowestCommonAncestor(root.left,p,q)
            
        elif max(p.val,q.val) > root.val:
            self.lowestCommonAncestor(root.right,p,q)
        
        return root
        
