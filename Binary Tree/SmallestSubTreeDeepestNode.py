'''
Given the root of a binary tree, the depth of each node is the shortest distance to the root.
Return the smallest subtree such that it contains all the deepest nodes in the original tree.
A node is called the deepest if it has the largest depth possible among any node in the entire tree.
The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
'''

'''
# Traverse Binary tree recursively using DFS.
# For every node calculate depth of the tree.
# At one node if you find left aub tree and right sub tree's depth equal then return it's root.
# If not then return maximum height amoung left and right sub tree and root of the maximim tree's height.
# Follow this process for all nodes, When you reach root node return main root node if height of left and right equal else maximum amoung them.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def depth_of_tree(self,root,depth = 0):
        
        if not root:
            return None,depth-1
        
        left,leftdepth = self.depth_of_tree(root.left,depth+1)
        right,rightdepth = self.depth_of_tree(root.right,depth+1)
        
        if leftdepth == rightdepth:
            return root,leftdepth
        
        return (left,leftdepth) if leftdepth > rightdepth else (right,rightdepth)
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        node,depth = self.depth_of_tree(root)
        
        return node
