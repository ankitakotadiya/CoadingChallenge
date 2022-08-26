'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
'''

'''
# The idea is DFS.
# Inililise one empty stack and level = 0.
# Make recursive call and check length of stack is less that level+1 then append one empthy array to store that particular level's node.
# Appen current node value at particular level into stack.
# Recursively traverse left and right node simultaneously pass level+1 and current stack.
# Once new level starts that means we have to append one empty list in the stack and store all the nodes at that level.
# At the end return stack.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
  
    def levelorderII(self,root):
      
      stack = [root]
      result = []
      
      while stack:
        node = stack.pop(0)
        result.append(node.val)
        
        if node.left:
          stack.append(node.left)
          
        if node.right:
          stack.append(node.right)
          
      return result
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        self.dfs(root,0,res)
        
        return res

    
    def dfs(self,root,level,res):
        
        if not root:
            return
        
        if len(res) < level + 1:
            res.append([])
            
        res[level].append(root.val)
        self.dfs(root.left,level+1,res)
        self.dfs(root.right,level+1,res)
