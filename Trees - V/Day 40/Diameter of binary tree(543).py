# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def find_max(node):
            if not node:
                return 0
            lh=find_max(node.left)
            rh=find_max(node.right)
            self.diameter=max(self.diameter,lh+rh)
            return 1+ max(lh,rh)
        find_max(root)
        return self.diameter