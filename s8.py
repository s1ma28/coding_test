#!/usr/bin/env python3
# *coding: utf-8
from typing import Awaitable, List
import math


class Solution:
    # 配列の大半（長さに対して、n/2以上）に頻出する値を返す
    # pre: nums = [3,2,3]
    # post: 3
    def majorityElement(self, nums: List[int]) -> int:
        # corner case: 配列要素1の場合

        map = {}

        # 1. linear scan left -> right.
        for num in nums:
            # 2. 既にmapに存在するなら、count値を+1
            if num in map:
                map[num] += 1
            # 3. mapに存在しないなら、新規でmapに追加 (要素値, 1=出現回数)
            else:
                map[num] = 1

        majority = math.floor(len(nums) / 2.0)
        majority_num = nums[0]
        # 4. mapのkey, valueを取得
        for key, val in map.items():
            # 5. 出現回数が大半だったkey値で、最初のものを取得
            if val > majority:
                majority_num = key

        return majority_num


if __name__ == '__main__':
    s = Solution()

    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
