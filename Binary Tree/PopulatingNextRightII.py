'''
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
'''

'''
# Create an empty stack and append root node.
# Also assign root to tail variable.
# run through loop until stack length greater than 0.
# now each and every iteration pop item at 0 index and push it's children into stack.
# Simultaneously check current poped node is equal to tail or not, if yes then the will always be rightmost node so set next pointer Null and update tail = rightmost pointer which is topmost element of the stack.
# If not then set current node's next pointer equal node at 0 index in stack.
# Follow same process for other ndes.
# At the end return root.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    
        
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        q = []
        
        q.append(root)
        
        tail = root
        while len(q) > 0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
            if node == tail:
                node.next = None
                tail = q[-1] if len(q) > 0 else None
            else:
                node.next = q[0]
                
        return root
