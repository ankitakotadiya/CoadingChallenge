'''
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
'''

'''
# Give a function to maximum bound inf.
# Left recursion will take element smaller than the it's root.
# Right recuresion rest smaller than bound.
# Return None if current value greater than bound.
# In each call increase increase current index i and bound for left children current node value and for right previous node value.
# At the end return root.

Time Complexity: O(n)
Space Complexity: O(h), height of tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    i = 0
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(A,bound):
            if self.i == len(A) or A[self.i] > bound:
                return None
            root = TreeNode(A[self.i])
            self.i += 1
            root.left = dfs(A, root.val)
            root.right = dfs(A, bound)
            return root
        
        return dfs(preorder,bound=float('inf'))
