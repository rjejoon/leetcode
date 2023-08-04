from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.max_diameter

    def depth(self, root):
        if root is None:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        self.max_diameter = max(
            self.max_diameter, left_depth + right_depth)

        return max(left_depth, right_depth) + 1
