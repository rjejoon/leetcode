from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        def dfs(node, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and sum(path) == targetSum:
                res.append(path.copy())
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return res
