from collections import deque
from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque()
        if root:
            d.append((root, 0))
        ret = []
        while d:
            node, lvl = d.popleft()
            if lvl < len(ret):
                ret[lvl].append(node.val)
            else:
                ret.append([node.val])
            if node.left:
                d.append((node.left, lvl+1))
            if node.right:
                d.append((node.right, lvl+1))

        return ret
