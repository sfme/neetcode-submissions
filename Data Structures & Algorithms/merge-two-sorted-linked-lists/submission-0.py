# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_list = ListNode()

        cur1 = list1
        cur2 = list2

        cur_merged = new_list

        while cur1 and cur2:

            if cur1.val < cur2.val:
                cur_merged.next = cur1
                cur1 = cur1.next
            else:
                cur_merged.next = cur2
                cur2 = cur2.next

            cur_merged = cur_merged.next

        if cur1:
            cur_merged.next = cur1

        else:
            cur_merged.next = cur2
        
        return new_list.next
 
        