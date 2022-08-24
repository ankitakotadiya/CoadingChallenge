'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

'''
# Initilise pointer p = None, which will be head of the merged list.
# Compare both lists first value and create a dummy node which stores smaller values and make pointer p refrencing to it.
# If list1 has smaller value then set pointer p's next node p.next = list1 and move list1 and pointer p to next node.
# Keep searching smaller value in both lists and append next to pointer p. Move next node which list has smaller value also move pointer p to next node.
# Once one of the list reached to it's end then append another list's remaining node to the pointer p.
# At the end return dummy.next.

Time Complexity: O(max(n1,n2)), n1 and n2 are number of nodes in list1 and list2
Space Complexity: O(1)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        d = ListNode()
        p = d
        
        while list1 and list2:
            
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
                
            else:
                p.next = list2
                list2 = list2.next
                
            p = p.next
        
        if list1:
            p.next = list1
        else:
            p.next = list2
            
        return d.next
