'''
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
'''

'''
# Run the loop till root is not null.
# Check root has left children or not.
# If yes then check it has right children or not.
# If yes,step further node until you get next right null.
# Set last right node's next node root node's right and set root node's left children null.
# Move root node's pointer further to right children and repeat above steps.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        while root != None:
            
            if root.left != None:
                p = root.left
                
                while p.right != None:
                    p = p.right

                p.right = root.right
                root.right = root.left
                root.left = None
                
            root = root.right
