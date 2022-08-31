'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

'''

'''
# The approach is DFS. 
# First will check target node less than root then will continue our traversal in left side otherwise right side.
# If target node is less than then will store previous node in successor while visit left side node.
# Now here we have two case.
# if right subtree node is not null then successor is it's minimum value means one of left child.
# If right subtree is null then successor is one of ancestors that we have previously store in successor.
# At the end return successor if right node is null otherwise right node's minimum value.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None

        while root != None and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        if root == None:
            return None

        if root.right == None:
            return successor


        root = root.right
        while root.left != None:
            root = root.left
        return root
