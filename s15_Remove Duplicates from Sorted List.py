#!/usr/bin/env python3
# *coding: utf-8
from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # 重複する値のノードを削除し、ユニーク値のみの連結リストを返す
    # pre: head = [1,1,2]
    # post: [1,2]
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # corner case: head is null
        if head is None or head.next is None:
            return head

        # 1: linear scan left -> right.
        curr = head
        while curr.next is not None:
            # 2-1: curr.val とcurr.next.valが同じかチェックする
            if curr.val == curr.next.val:
                # 3: 次ノードがNoneかチェック。-> while文でチェックしているため不要

                # 4: 次々ノードがNoneかチェック。-> 不要。Noneだとしてもcurr.next.next = None と値が入っているから。
                # curr.next = curr.next.next として次ノードをskipする（ガーベージにいずれ回収される＝削除）
                # if curr.next.next is not None:
                curr.next = curr.next.next
                # else:
                #     curr.next = None

            # 2-2: curr.val とcurr.next.valが異なる場合は、そのまま次ノードへ移動
            else:
                curr = curr.next

        return head
