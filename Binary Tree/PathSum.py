'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
'''

'''
# Recursively move left and right subtree, in each call increase the sum by value of current node.
# If at any level current node equal to leaf node and sum equal to target sum then return True.
# Otherwise check sum in right sub tree.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def targetsum(self,root,tsum,summ):
        
        if not root:
            return False
        
        summ = summ + root.val
        
        if not root.left and not root.right:
            
            if tsum == summ:
                return True
            
        return self.targetsum(root.left,tsum,summ) or self.targetsum(root.right,tsum,summ)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.targetsum(root,targetSum,0)
