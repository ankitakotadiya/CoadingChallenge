'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
'''

'''
# The idea is DFS.
# Create one empty array to store right view of binary tree.
# To track right view on each level create one max_level, initially set -1.
# Let's say current node is p and level = 0.
# Now check if max_level less than level then append p.val to our result and update max_level = current level
# Recursevly call first right child then left also update level by one.
# In the next level max_level = 0 and current level 1 so will append p.val to the result and update max_level = 1.
# So when we see left child on the same level it will not append value because max_level and current level are same. 
# Traverse all the nodes and return result.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        max_level = -1
        
        def traversal(root,level):
            
            nonlocal res,max_level
            if not root:
                return
            
            if max_level < level:
                res.append(root.val)
                max_level = level
                
            traversal(root.right,level+1)
            traversal(root.left,level+1)
         
        traversal(root,0)
        return res
