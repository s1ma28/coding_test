#!/usr/bin/env python3
# *coding: utf-8

from typing import List


class Solution:
    # return true if nums[] contains duplicate
    # pre: nums[1,2,3,1]
    # post: true
    def containsDuplicate(self, nums: List[int]) -> bool:
        # corner case: nums is empty or size 1, return false
        if len(nums) <= 1:
            return False

        map = {}

        # step1: single linear scan left -> right, build hashMap as we go
        # testcase: nums[1,2,3,1], num=1,map[]
        # testcase: nums[1,2,3,1], num=2,map[(1,True)]
        # testcase: nums[1,2,3,1], num=3,map[(1,True),(2,True)]
        # testcase: nums[1,2,3,1], num=1,map[(1,True),(2,True),(3,True)]

        for num in nums:
            # step2: if map containsKey(num[i]) == true, then dup found.
            if num in map:
                return True

            map[num] = True

        return False
