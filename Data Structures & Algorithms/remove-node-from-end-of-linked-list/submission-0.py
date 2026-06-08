# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        new_list = ListNode(0, head)
        left_p = new_list

        k = n
        right_p = head

        while k > 0:
            right_p = right_p.next
            k -= 1

        
        while right_p:
            left_p = left_p.next
            right_p = right_p.next

        # removes element
        left_p.next = left_p.next.next
        
        return new_list.next  