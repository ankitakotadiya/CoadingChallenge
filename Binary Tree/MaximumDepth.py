'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
'''

'''
# The idea is DFS.
# Traverse left and right node recursively and return max height of left right node plus one at each node.
# So when you reach last node you will get maximum depth.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        if l > r:
            return l+1
        else:
            return r+1
