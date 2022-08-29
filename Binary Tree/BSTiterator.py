'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
'''

'''
# If we do inorder traversal of BST then will get sorted array in result.
# Store sorted list in variable called values.
# Set initial pointer equal to 0 and length equal to number of elements in values.
# Now if function called next so first we need to check our pointer should be less than the length of values.
# If yes then return value at pointer simultaneously increase pointer by one.
# If function called hasnextvalue then agian check same condition pointer should be less than values, if yes then return True else False.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:

    def inorder(self,root):
        
        if not root:
            return []
        
        else:
            
            left = self.inorder(root.left)
            right = self.inorder(root.right)
            
            left.append(root.val)
            left.extend(right)
            
        return left
    
    def __init__(self, root: Optional[TreeNode]):
        
        self.values = self.inorder(root)
        self.pointer = 0
        self.length = len(self.values)
        

    def next(self) -> int:
        
        if self.pointer < self.length:
            value = self.values[self.pointer]
            self.pointer += 1
            return value
        return None
        

    def hasNext(self) -> bool:
        
        if self.pointer < self.length:
            return True
        
        return False
