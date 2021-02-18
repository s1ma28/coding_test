#!/usr/bin/env python3
# *coding: utf-8

from typing import List


class Solution:
    # 足すとtarget値になる2つの値のインデックスを返す
    # pre: nums = [2,7,11,15], target = 9
    # post: [0,1]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # corner case: 配列が1以下の場合
        if len(nums) <= 1:
            return -1

        map = {}
        results = []
        for i, num in enumerate(nums):
            complement = target - nums[i]
            # testcase: nums=[3,2,4],target=6,i=0,complement=3,map={}
            # testcase: nums=[3,2,4],target=6,i=1,complement=4,map={(3,0)}
            # testcase: nums=[3,2,4],target=6,i=2,complement=2,map={(3,0),(2,1)}
            if complement in map:
                # 値がmapに存在していた場合、2つのインデックスをresultsに追加
                # map[complement]=1, i=2
                results.append(map[complement])
                results.append(i)
            else:
                # arrayをmap化。(値:インデックス)
                # testcase: nums=[3,2,4],target=6,i=0,complement=3,map={(3,0)}
                # testcase: nums=[3,2,4],target=6,i=1,complement=4,map={(3,0),(2,1)}
                map[num] = i

        return results


if __name__ == '__main__':
    s = Solution()

    print(s.twoSum([3, 2, 4], 6))
