'''
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
'''

'''
# This method is only work for complete binary tree.
# First we set next pointer of it's children before we start traversing it's children.
# When we are at node p, we set next of it's left and right.
# Since tree is complete tree so, next of p's left child will always be p's right child and next of p's right child will always be left child of p's next pointer.
# If node p is rightmost then it's next pointer will be Null.

Time Complexity: O(n)
Space Complexity: O(1)

'''

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    
    def dfs(self,root):
        
        if root is None or root.left is None:
            return
        
        root.left.next = root.right
        print(root.left.next.val)

        if root.next is not None:
            # print(root.next.val)
            root.right.next = root.next.left
            # print(root.next.left.val)
            
        self.dfs(root.left)
        self.dfs(root.right)
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        self.dfs(root)
        return root
