from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return None
        tot = 0
        if root.val >= low and root.val <= high:
            tot += root.val
        right_tot = self.rangeSumBST(root.right, low, high)
        if right_tot:
            tot += right_tot
        left_tot = self.rangeSumBST(root.left, low, high)
        if left_tot:
            tot += left_tot
        return tot
