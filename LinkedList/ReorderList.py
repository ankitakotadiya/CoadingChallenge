'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''

'''
# First will use slow and fast pointer to find out mid value of linked list.
# Once we get mid node, reverse all nodes just after it.
# Set null next node of mid point to null so we have one list till mid.
# Initilise two pointer one holds head to mid and other one reversed list after mid point.
# Set reversed list next node equal to head's next node and head's next node equal to head of reversed list.
# Follow the process till one of or both list point to next node null.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        cur = slow.next
        prev = None
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        slow.next = None
        
        n1 = head
        n2 = prev
        
        while n1 and n2:
            n1next = n1.next
            n2next = n2.next
            
            n2.next = n1.next
            n1.next = n2
            
            n1 = n1next
            n2 = n2next
            
        if n1:
            n1.next = None
