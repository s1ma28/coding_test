#!/usr/bin/env python3
# *coding: utf-8
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # Treeの最長の深さを調べて返す。Bottom-Upアプローチ
    # pre: root = [3,9,20,null,null,15,7]
    # post: 2
    def maxDepth(self, root: TreeNode) -> int:
        def maxDepthRecursive(root: TreeNode) -> int:
            # base case: root is none, return 0
            if root is None:
                return 0

            # best case: root is last. return 1. ⇒ 不要？ ⇒ ありでもできる。leftとrightの余分な処理が減るだけ
            if root.left is None and root.right is None:
                return 1

            # left: leftの子をrootとして、左側のもう1回maxDepthRecursiveをやる
            left_maxDepth = maxDepthRecursive(root.left)

            # right: rightの子をrootとして、右側の範囲でもう1回maxDepthRecursiveをやる
            right_maxDepth = maxDepthRecursive(root.right)

            # left と rightの結果で大きかった方を選び、現階層の分+1して、呼び出し元に返す
            return max(left_maxDepth, right_maxDepth) + 1

        return maxDepthRecursive(root)
