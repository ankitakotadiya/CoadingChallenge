'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
'''

'''
# The approach is DFS.
# Recursively traverse left and right sub tree.
# In each call keep track of sum by sum * 10 plus current node's value till leaf node
# So each and node has calculated value from root to current node.
# So at root node return sum of left tree plus right tree.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def sumnodes(self,root,prevsum,summ):
        
        if root is None:
            return prevsum
        
        summ = summ*10 + root.val
        
        if not root.left and not root.right:
            
            prevsum = prevsum + summ
            return prevsum
        
        return self.sumnodes(root.left,prevsum,summ) + self.sumnodes(root.right,prevsum,summ)
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        return self.sumnodes(root,0,0)
