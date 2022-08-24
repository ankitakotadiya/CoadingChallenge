'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
'''

'''
# Create one empty hashmap to store copy of each node.
# Assign head of linked list to cur.
# Get one by one node and create a copy of that node save key as old node value as copy of that node.
# Once copy of all nodes done then set back cur = head of the linked list.
# iterate one by one node search copy of old node and set it's next pointer as well random pointer.
# At the end return copy node's head.

Time Complexity: O(2n)
Space Complexity: O(n)
'''

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        cur = head
        Map = {None:None} 
        
        while cur:
            copy = Node(cur.val)
            Map[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = Map[cur]
            copy.next = Map[cur.next]
            copy.random = Map[cur.random]
            cur = cur.next
            
        return Map[head]
