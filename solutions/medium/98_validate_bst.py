from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.inorder(root)

    def inorder(self, root):
        if root is None:
            return True

        if not self.inorder(root.left):
            return False
        if not root.val > self.prev:
            return False
        self.prev = root.val
        return self.inorder(root.right)
