#!/usr/bin/env python3
# *coding: utf-8
from typing import List

# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # 片方向連結リストの真ん中にあたるノード(値ではなくオブジェクト)を返す。(偶数時は[1,2,3,4]なら、3が真ん中)
    # pre: [1,2,3,4,5]
    # post: Node 3 from this list (Serialization: [3,4,5]
    def middleNode(self, head: ListNode) -> ListNode:

        # corner case: head、head.nextがnull
        if head is None or head.next is None:
            return head

        slow = head
        fast = head

        values = []
        # 1: fast.nextとfast.next.nextがnullでない間、fastとslowのポインタを右へ進める
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        middle = head
        # 2: nullがfast.nextとfast.next.nextのどちらにあるかをチェックする（evenかoddかが分かる）
        if fast.next == None:
            # odd
            middle = slow
        else:
            # 3: even時ならslowを右へ1つずらす
            # even
            middle = slow.next

        # 4: slowの値を真ん中として返す
        return middle


if __name__ == '__main__':
    s = Solution()

    print(s.middleNode(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    print(s.middleNode(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
