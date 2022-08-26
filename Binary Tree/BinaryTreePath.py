'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
'''

'''
# Use result array to store path from root to leaf.
# Traverse tree from root to leaves.
# when you reach leaf append the root to leaf path in result.
# All nodes hold path from root to current node.
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if root is None:
            return []
        
        elif not root.left and not root.right:
            return [str(root.val)]
        
        else:
            
            left = self.binaryTreePaths(root.left)
            right = self.binaryTreePaths(root.right)
            
            result = []
            
            for path in left:
                val = str(root.val) + '->' + path
                result.append(val)
                
            for path in right:
                val = str(root.val) + '->' + path
                result.append(val)
                
            return result
