'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Input: root = [1,2,3,4,5,null,null]
Output: [4,5,2,3,1]
'''

'''
# Create a stack and push root node.
# Run the loop until stack is not empty.
# Each and every iteration pop item from the stack and append that item in our result.
# Check whether popped item has left and right element or not if yes then pushed into stack.
# Follow same steps in next iteration.
# At the end return reversed of result.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
  
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack1 = []
        stack2 = []
        stack1.append(root)
        
        while stack1:
            
            node = stack1.pop()
            
            if node:
                stack2.append(node.val)
                
                if node.left:
                    stack1.append(node.left)
                    
                if node.right:
                    stack1.append(node.right)
                
        return stack2[::-1]
      
  def postorderTraversalII(self, root: Optional[TreeNode]) -> List[int]:

          stack1 = []
          stack2 = []
          stack1.append(root)

          while stack1:

              node = stack1.pop()

              if node:
                  stack2.insert(0,node.val)

                  if node.left:
                      stack1.append(node.left)

                  if node.right:
                      stack1.append(node.right)

          return stack2
