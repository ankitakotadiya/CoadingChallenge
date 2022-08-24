'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''

'''
# The approach is fast and slow pointer.
# Move slow pointer to one step and fast pointer to two steps each time.
# When fast and slow pointer meet at one point p, the length they have run are a+2b+c and a+b.
  Where a is head of the list to the cycle begin distance. b is begining of cycle to the meet point. c is meet point to begining of cycle distance.
  
# Since fast is two times faster than slow so a+2b+c = 2(a+b) we get a = c so if we assign head to the slow pointer and move both pointer to one step each time then they would meet at begining of the cycle.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
            
        return head
