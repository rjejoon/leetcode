from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: i for i, val in enumerate(inorder)}

        def divide_and_conquer(pre_left, pre_right, in_left):
            if pre_left > pre_right:
                return None

            if pre_left == pre_right:
                return TreeNode(preorder[pre_left])

            # mid is always the first element in preorder
            mid = TreeNode(preorder[pre_left])
            # find left
            i = inorder_index_map[preorder[pre_left]]
            mid.left = divide_and_conquer(
                pre_left+1, pre_left+i-in_left, in_left)
            # rest are on the right subtree of the mid
            mid.right = divide_and_conquer(
                pre_left+i-in_left+1, pre_right, i+1)

            return mid

        return divide_and_conquer(0, len(preorder)-1, 0)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(Solution().buildTree(preorder, inorder))
