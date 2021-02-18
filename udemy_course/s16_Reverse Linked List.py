#!/usr/bin/env python3
# *coding: utf-8
from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # 連結リストを逆順にして、その先頭のノードを返す
    # pre: head (1->2->3->4->5->NULL)
    # post: head (5->4->3->2->1->NULL)
    def reverseList(self, head: ListNode) -> ListNode:
        # corner case: head is null, head.next is null
        if head is None or head.next is None:
            return head

        # 1: 3 pointer 。農具の「クワ」パターン。常に並んで横へ移動する
        prev = None
        curr = head
        next = curr.next

        # 2: linear scan left -> right. currがnullになるまでループ
        while curr is not None:
            # 3: 矢印の向きを逆にする。「prev -> curr」を「prev <- curr」にする
            # testcase1: 1->2->3->4->5->NULL, prev=null,curr=1,next=2, curr.next=null
            # testcase1: 1->2->3->4->5->NULL, prev=1,curr=2,next=3, curr.next=1
            # testcase1: 1->2->3->4->5->NULL, prev=2,curr=3,next=4, curr.next=2
            # testcase1: 1->2->3->4->5->NULL, prev=3,curr=4,next=5, curr.next=3
            # testcase1: 1->2->3->4->5->NULL, prev=4,curr=5,next=None, curr.next=4
            # testcase1: 1->2->3->4->5->NULL, prev=5,curr=None,next=None, curr.next=5
            curr.next = prev

            # 4: 3ポインタ(クワ)を横へ移動する。nextがnullの場合、next = None
            prev = curr
            curr = next

            if next is not None:
                next = next.next

        # 5: head = prevとして、返す
        head = prev

        return head
