# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, max_so_far: int) -> int:

            if not node:
                return 0

            if node.val >= max_so_far:
                good = 1
                max_so_far = node.val

            else:
                good = 0

            left_count = dfs(node.left, max_so_far)
            right_count = dfs(node.right, max_so_far)

            return good + left_count + right_count

        return dfs(root, root.val)