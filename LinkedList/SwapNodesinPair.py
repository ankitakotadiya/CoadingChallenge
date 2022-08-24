'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''

'''
# Create one dummy node whose next pointer will be the head of the linked list.
# Now take a current node which will use to traverse the list.
# In each iteration take two nodes first and second and swap them. Move current node by two pointer as we already swapped two nodes.
# Again will get two nodes swap them, follow the same process till we reached to the end of the linked list.
# Return dummy node's next pointer.
'''

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        senital = ListNode(0,head)
        prev = senital
        while prev.next and prev.next.next:
            fn = prev.next
            sn = prev.next.next
            
            fn.next = sn.next
            prev.next = sn
            prev.next.next = fn
            
            prev = prev.next.next
            
        return senital.next

