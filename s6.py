#!/usr/bin/env python3
# *coding: utf-8
from typing import List


class Solution:

    # 0をarray末尾へ全て移動する。in-placeで。
    # pre: [0,1,0,3,12]
    # post: [1,3,12,0,0]
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        runner_index = 0
        zero_index = 0
        # step1: arrayをlinear scan
        while runner_index < len(nums):

            if nums[runner_index] != 0:
                # step2: 値が0以外なら、0の位置と値を入れ替える
                nums[runner_index], nums[zero_index] = nums[zero_index], nums[runner_index]

                # step3: 両方のポインタを右へ1ずらす
                zero_index += 1

            runner_index += 1

        return nums


if __name__ == '__main__':
    s = Solution()

    print(s.moveZeroes([0, 1, 0, 3, 12]))
