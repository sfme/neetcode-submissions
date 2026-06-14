# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k = k
        self.result = None
        
        def inorder(node):
            if not node or self.result is not None:
                return
            
            # traverse left
            inorder(node.left)
            
            # process root
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            
            # traverse right
            inorder(node.right)
            
        inorder(root)
        
        return self.result