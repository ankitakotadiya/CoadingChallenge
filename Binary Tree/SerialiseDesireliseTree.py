'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
'''

'''
# In the serialise process will do preorder traversal using DFS.
# Will use one array to store root and it's children.
# Once left and right children reach to null means no next node will apeend 'n' to our resultant array.
# Convert array to string.

# Deserialise process we have serialised string convert string to array.
# Same will follow preorder traversal and will access one by one element from array using pointer which is initially 0.
# Will increase pointer value by one in each call.
# Once we see element 'n' in left recusion call then will set left child null else right.
# Follow the same process for rest element.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        
        def dfs(node):
            
            if node is None:
                nodes.append('n')
                return
             
            nodes.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        if root is None:
            return ''
        nodes = []
        dfs(root)
        print(nodes)
        
        return ','.join(nodes)
            

    def deserialize(self, data):
        
        if len(data) == 0:
            return None
        nodes = data.split(',')
        def dfs():
            if nodes[cur_pos[0]] == 'n':
                cur_pos[0] += 1
                return None
            root = TreeNode(int(nodes[cur_pos[0]]))
            cur_pos[0] += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        cur_pos = [0]
        return dfs()
