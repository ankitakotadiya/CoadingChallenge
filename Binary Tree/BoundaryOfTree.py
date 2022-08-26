'''
Your task is to write a program that reads a perfect binary tree and prints the values of all nodes on the outer "edges" of the tree in counterclockwise order, starting at the root. You should try to do this as efficiently as possible.

'''

'''
# The idea is to recursevely call left sub tree and append all left nodes in result array.
# Store all the leaf node which has left and right child none. So recursively call left and right sub tree and append leaf nodes in result array.
# Same recursively call right sub tree and append right nodes in result array.
# At the end return result.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
  
  def __init__(self):
    self.result = []
    
    
  def print_leftboundary(self,root):
    
    if not root :
      return
    
    if root.left:
      self.arr.append(root.val)
      self.print_leftboundary(root.left)
      
    elif root.right:
      self.arr.append(root.val)
      self.print_leftboundary(root.right)
      
  def print_rightboundary(self,root):
    
    if not root :
      return
    
    if root.right:
      self.arr.append(root.val)
      self.print_leftboundary(root.right)
      
    elif root.left:
      self.arr.append(root.val)
      self.print_leftboundary(root.left)
      
  def print_leaves(self,root):
    
    if not root :
      return
    
    if root.right is None and root.left is None:
      self.arr.append(root.val)
      
    self.print_leaves(root.left)
    self.print_leaves(root.right)
    
  def print_boundary(self,root):
    
    if not root:
      return self.result
    
    self.result.append(root.val)
    self.print_leftboundary(root.left)
    self.print_leaves(root)
    self.print_rightboundary(root.right)
    
    return self.result

