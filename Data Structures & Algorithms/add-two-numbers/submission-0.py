# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

            carry_over = 0

            new_list = ListNode()
            cur = new_list

            while l1 or l2 or carry_over:

                v1 = l1.val if l1 else 0
                v2 = l2.val if l2 else 0

                sum_vals = v1 + v2 + carry_over

                cur.next = ListNode(sum_vals % 10, None)

                carry_over = sum_vals // 10 

                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
                cur = cur.next

            return new_list.next