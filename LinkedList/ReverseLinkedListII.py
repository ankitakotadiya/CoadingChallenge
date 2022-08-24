'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
'''

'''
# Create one node which point to the head of linked list.
# Create one start pointer initially set Null.
# Move pointer to the next till you reach left position. Each and evry time update start pointer so when you reach at left position start pointer holds just before node value.
# Set previous and end node equal to the that left position node. Move current node by one step to the next next.
# Reverse all the node till right position.
# Nodes remains after right position set after reversed node.
# We have start node just before left position node, connect start's next node equal to reverse node.
# At the end return head.

Time complexity: O(n)
Space Complexity: O(n)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head:
            return head
        node = head
        start = None
        pos = 1
        while pos < left:
            start = node
            node = node.next
            pos += 1
        end = node
        prev_node = node
        node = node.next
        pos += 1
        while node and pos <= right:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
            pos += 1
        end.next = node
        if start:
            start.next = prev_node
            return head
        else:
            return prev_node
