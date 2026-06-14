"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node

        map_old_to_new = dict()

        def dfs(node):

            if node in map_old_to_new:
                return map_old_to_new[node]

            new = Node(node.val)
            map_old_to_new[node] = new

            for neighbor in node.neighbors:
                new.neighbors.append(dfs(neighbor))

            return new

        return dfs(node)


        