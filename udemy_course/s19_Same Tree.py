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
    # ツリー構造（左右のノードの位置、値）が全て一致しているかどうかを判定する。top-downアプローチ
    # pre: p = [1,2,3], q = [1,2,3]
    # post: true
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def isSameTreeRecursive(p: TreeNode, q: TreeNode) -> bool:
            # base case: p is None && q is None なら、再帰終了
            if p is None and q is None:
                return True

            # 片方のみNoneの場合（Nullpointer回避用）
            if p is None or q is None:
                return False

            # 1: p.val と q.val が不一致なら、配下を探索するまでもなくツリーが一致していないので、再帰終了
            if p.val != q.val:
                return False

            # 2: p.val と q.valが一致しているなら、配下の左右に対しても再帰
            return isSameTreeRecursive(p.left, q.left) & isSameTreeRecursive(p.right, q.right)

        return isSameTreeRecursive(p, q)
