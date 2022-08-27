'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
'''

'''
# The approach is DFS.
# Recursively visit left and right childrens and calculate their maximum path.
# Root node of every subtree, we need to return maximum path such that root node value plus maximum value among left child and right simultaneously store maximum path of that subtree.
# Maximum sum can be calculated by left child + right child + root node.
# So when you reach root node you have maximum sum also left subtree's maximum root path and right sub tree's maximum root path.
# Return left sub tree to root if sum is max.
# Return right sub tree if sum is max.
# If current max_sum left subtree + root node + right sub tree then save max path equal to left + right + root and return it.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def dfs(self, node):
        if not node: return 0
        
        left = self.dfs(node.left)
        left = max(left,0)
        right = self.dfs(node.right)
        right = max(right,0)

        val = left + right + node.val
        self.max_sum = max(self.max_sum, val)
        
        return max(left, right) + node.val
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
