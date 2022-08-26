'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
'''

'''
# The idea is DFS.
# Traverse both tree simultaneoulsly.
# Recursively traverse left and right node, when you reach left node and right node are node None, this is our leaf node, save in array.
# Follow same process for the another tree.
# At the end compare both tree if both matched then return True else False.

Time Complexity: O(n)
Space Complexity: O(h), where h is max of max(h1,h2) number of leaf nodes in both trees.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if not root1 and not root2:
            return True
    
        if not root1 or not root2:
            return False

        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [node.val]


            return dfs(node.left) + dfs(node.right)

        return dfs(root1) == dfs(root2)
