'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
'''

'''
# The basic approach is DFS.
# Recursively traverse left and right sub tree.
# In each call kepp track of path that led to current node.
# At each node will check path whose sum equals to target sum for that will store root to current node's total in hashmap.
# If we found any path then increase count for that node.
# Follow same process in right sub tree.
# Once left and right sub tree of current node is traversed then remove total of that node.
# At the root node node return count of left sub tree plus right sub tree.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        sums = defaultdict(int)
        sums[0] = 1
        
        def dfs(root,total):
            
            count = 0
            
            if root:
                
                total += root.val
                
                count = sums[total-targetSum]
                
                sums[total] += 1
                
                count += dfs(root.left,total) + dfs(root.right,total)
                
                sums[total] -= 1
                
            return count
        
        return dfs(root,0)
