#!/usr/bin/env python3
# *coding: utf-8
from typing import List


class Solution:
    # valの重複値をin-placeで削除し、削除後の要素数を返す
    # pre: nums = [3,2,2,3], val = 3
    # post: 2, nums = [2,2]
    def removeElement(self, nums: List[int], val: int) -> int:
        # corner case: 長さが1以下の場合、

        runner_index = 0
        target_index = 0
        # step1: linear scan left -> right
        while runner_index < len(nums):
            # step2: nums[runner_index]の値がvalと一致しなければ、swap
            # testcase1: nums=[3,2,2,3], val=3, ri=0, ti=0, nums[ri]=3, nums[ti]=3
            # testcase1: nums=[3,2,2,3], val=3, ri=1, ti=0, nums[ri]=2, nums[ti]=3
            # testcase1: nums=[2,3,2,3], val=3, ri=2, ti=1, nums[ri]=2, nums[ti]=3
            # testcase1: nums=[2,2,3,3], val=3, ri=3, ti=2, nums[ri]=3, nums[ti]=3

            if nums[runner_index] != val:
                nums[runner_index], nums[target_index] = nums[target_index], nums[runner_index]
                target_index += 1

            runner_index += 1

        return target_index


if __name__ == '__main__':
    s = Solution()

    print(s.removeElement([3, 2, 2, 3], 3))
    print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
