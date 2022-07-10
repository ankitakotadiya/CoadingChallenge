class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x) if x>=0 else None
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
        
#         if head is None:
#             return
#         clone = head
#         clone.random = head.random
#         clone.next = self.copyRandomList(head.next)
        
#         return clone
