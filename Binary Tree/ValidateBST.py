'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true
'''

'''
# Here will use inorder to traverse every node of tree and store in array.
# If we do inorder of BST will always get sorted array.
# Now run through loop check value place at index i should be smaller than value placed at index i+1.
# If condition doesn't match then return False else True.

Time Complexity: O(n)
Space Complexity: O(1)
'''

# Another Solution
'''
# In BST left child value always less than it's parent and right child always greater than parent.
# Initially will set lower = -inf and upper  = inf
# recuresively traverse and left and right children.
# While traversing left child will set upper = current and for right will update lower = current node.
# If condition matched like current node less than lower and upper > current node then will continue traversing else return False because tree is not valid.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    
    def helper(self,node, lower, upper):
            
        if not node:
            return True

        if lower < node.val < upper:
            return self.helper(node.left, lower, node.val) and self.helper(node.right, node.val, upper)

        else:
            return False
    
    def inorder(self,root,output):
        
        if not root:
            return 
        
        self.inorder(root.left,output)
        output.append(root.val)
        self.inorder(root.right,output)
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        output = []
        self.inorder(root,output)
        
        for i in range(1,len(output)):
            
            if output[i-1] >= output[i]:
                return False
        return True
