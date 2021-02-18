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
    # 指定した値と一致するvalを持つノードを返す。配下のノードも付いたまま。
    # pre: root = [4,2,7,1,3], val = 2
    # post: [2,1,3]
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def searchBSTRecursive(root: TreeNode, val: int) -> TreeNode:
            # base case: root is null
            if root is None:
                return root

            # baet case: root.val == val の場合、return root
            if root.val == val:
                return root

            # 2: root.val < val で右側のツリーだけで再帰。searchBST(root.right, val)
            if root.val < val:
                return searchBSTRecursive(root.right, val)

            # 3: root.val < val で左側のツリーだけで再帰。searchBST(root.left, val)
            if val < root.val:
                return searchBSTRecursive(root.left, val)

        return searchBSTRecursive(root, val)
