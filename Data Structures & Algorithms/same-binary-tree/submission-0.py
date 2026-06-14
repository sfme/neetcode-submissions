# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both null, same
        if not p and not q:
            return True
        
        # one is null, not equal
        if not p or not q:
            return False
        
        # the values don't match, not equal
        if p.val != q.val:
            return False
        
        # check if left and right subtrees match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)