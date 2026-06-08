# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_p = head
        fast_p = head.next

        # mid point of list
        while fast_p and fast_p.next:
            
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        half_p = slow_p.next
        slow_p.next = None

        # reverse 2nd part of list
        prev = None
        cur = half_p

        while cur:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp

        half_p_reversed = prev
    
        # new list: alternated merge of lists
        cur1 = head
        cur2 = half_p_reversed

        while cur2:

            # Temporarily store the original 'next' nodes
            temp1 = cur1.next
            temp2 = cur2.next

            # Re-wire the pointers to weave them together
            cur1.next = cur2
            cur2.next = temp1

            # Advance cur1 and cur2 forward using our saved temp variables
            cur1 = temp1
            cur2 = temp2
        




