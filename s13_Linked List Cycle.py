#!/usr/bin/env python3
# *coding: utf-8
from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # 連結リストがサイクルしているかを判定する関数
    # pre: head = [3,2,0,-4], pos = 1
    # post: true
    def hasCycle(self, head: ListNode) -> bool:
        # corner case: head, head.next is empty
        if head is None or head.next is None:
            return False

        # 1: 連結リストを2つのポインタで辿る。fast、slow
        slow = head
        fast = head.next
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

            # 2: fastとslowが同じノードになった場合、サイクルしているとしてreturn True
            if fast == slow:
                return True

        # 3: ループが終わっているため、サイクルしていないのでFalse
        return False


if __name__ == '__main__':
    pass
