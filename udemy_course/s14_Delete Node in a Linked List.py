#!/usr/bin/env python3
# *coding: utf-8
from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 与えられたノードを削除（次のノードの値で上書き）する。in-place。returnなし。headなし。
    # pre: node = 1  (head = [4,5,1,9])
    # post: [4,1,9]
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 1: 次ノードがNoneなら、何もしない
        if node.next is None:
            return

        # 2: 次ノードがNoneでないなら、次ノードの値で今ノードの値を上書きする
        # nodeNextNext = node.next.next
        node.val = node.next.val
        node.next = node.next.next
