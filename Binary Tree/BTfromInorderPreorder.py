'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
'''

'''
# First of all using hashmap i will store value as key and index as value.
# Now using DFS set root, left and right children.
# We know that, first element of preorder is the root of the tree.
# Now search preorder's leftmost element in inorder list as we have already created hashmap so will get index of it, which would become our mid point. 
# So all the elements till mid become left children and after mid right children.
# make recursive call of left half and right half of both the arrays and set left and right children.
# At the end return root.

Time Complexity: O(n)
Space Complexity: O(n)
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        dic = {}
        
        for i,v in enumerate(inorder):
            dic[v] = i
            
        def dfs(preorder,inorder):
            
            nonlocal dic
            if not inorder or not preorder:
                return None

            root = TreeNode(preorder[0])
            mid = dic[preorder[0]]

            root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
            root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
            
            return root
        
        return dfs(preorder,inorder)
