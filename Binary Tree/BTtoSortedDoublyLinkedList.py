'''
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

'''

'''
# The approach is DFS.
# Will create one dummy node and point to prev variable.
# Now recursively visit left and right node and when you see left child's next pointer reach to null set prev's right equal to current node and current node's left to prev and move prev to current node.
# Once inorder traversal done then connect previous tail to dummy's head.
# Return dummy node's right node.

Time Complexity: O(n)
Space Complexity: O(h)
'''

class TreeNode:
  
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None
    
class Solution:
  
  def BinaryTreetoDLL(self,root):
    
    dummy = TreeNode(-1)
    prev = dummy
    
    def inorder(cur):
      
      nonlocal prev
      
      if not cur:
        return
      
      inorder(cur.left)
      
      prev.right = cur
      cur.left = prev
      prev = cur
      
      inorder(cur.right)
      
    prev.right = dummy.right
    dummy.right.left = prev
    
    return dummy.right
