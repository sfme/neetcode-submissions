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

        dict_nodes = collections.defaultdict(lambda: Node(0))
        dict_nodes[None] = None
        
        cur = head
        while cur:

            dict_nodes[cur].val = cur.val
            dict_nodes[cur].next = dict_nodes[cur.next]
            dict_nodes[cur].random = dict_nodes[cur.random]

            cur = cur.next

        return dict_nodes[head]
        