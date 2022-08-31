'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
'''

'''
1. BFS Solution
  # The approach is BFS. Will use stack and dummy nodes temp and x which point to root node of our tree.
  # Move pointer temp towards left until find null and each iteration push into stack.
  # Once we see left child's next node is null that time will pop an element from stack set it our root node of dummy x. Simultaneously will check if it has any right node then append into stack.
  # Pop an element from stack if no left child and set next right of x and set left child null.
  # Continue follow the process until stack is non-empty.
  # At the end return root.
  
  Time Complexity: O(n)
  Space Complexity: O(n)
  
2. DFS Solution
  # Here will create dummy node and point to prev variable.
  # Recursively traverse left and right children and set prev's right node equal to current node and left none.
  # Return dummy node's right node.
  
  Time Complexity: O(n)
  Space Complexity: O(h), height of tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  
    def increasingBSTDFS(self, root: TreeNode) -> TreeNode:
        
        dummy = TreeNode(-1)
        
        prev = dummy
        
        def inorder(cur):
            
            nonlocal prev
            if cur is None:
                return 
            
            inorder(cur.left)
            
            prev.left = None
            prev.right = cur
            prev = cur
            
            inorder(cur.right)
            
        inorder(root)
        prev.left = None
        prev.right = None
        return dummy.right
      
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        stack = []
        temp = x = root
        i = 0
        
        while stack or temp:
            
            if temp:
                stack.append(temp)
                temp = temp.left
                
            else:
                node = stack.pop()
                if i == 0:
                    
                    root = x = node
                    i+=1
                    
                else:
                    
                    x.right = node
                    x = node
                    x.left = None
                    
                temp = node.right
                
        return root
