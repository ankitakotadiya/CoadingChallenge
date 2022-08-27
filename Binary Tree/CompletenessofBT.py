'''
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
'''

'''
# The approach is BST.
# I will use one empty stack initially push root node of the tree.
# Run through loop until stack is non-empty.
# Each and every iteration pop item at index 0 and check whether is null or not.
# If it is null then continue iteration check next element if it is not null then return False tree is not complete.
# Because if we get any null node between non null nodes then tree is not complete.
# If not null then push their children into stack.
# Continue follow this process and at the end return True.

Time Complexity: O(n)
Space Complexity: O(n)
'''

def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return
        
        stack = []
        have_null = False
        stack.append(root)
        
        while(len(stack) > 0):
            
            node = stack.pop(0)
            
            if not node:
                have_null = True
                continue
            
            if have_null:
                return False
            
            stack.append(node.left)
            stack.append(node.right)
                
        return True
