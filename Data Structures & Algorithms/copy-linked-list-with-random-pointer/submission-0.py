"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dict_nodes = {None: None}

        cur = head
        while cur:
            dict_nodes[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:

            node_copy = dict_nodes[cur]
            node_copy.next = dict_nodes[cur.next]
            node_copy.random = dict_nodes[cur.random]

            cur = cur.next

        return dict_nodes[head]
        