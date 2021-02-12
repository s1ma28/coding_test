#!/usr/bin/env python3
# *coding: utf-8
from typing import List


class Solution:
    # 2つのarrayで共通する要素を返す。ユニーク。順不同。
    # pre: nums1 = [1,2,2,1], nums2 = [2,2]
    # post: [2]
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # corner case: empty
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        # 1: nums1のみ、map化する
        map = {}
        for num in nums1:
            map[num] = False

        result = []
        # 2: nums2をlinear scan left -> right.
        for num in nums2:
            # 3: nums2の要素が、map内のkeyと同じ、かつそのkeyの値がFalseか、チェックする（Falseは未抽出の印。Trueは抽出済）
            # testcase2: map={4:False,9:True,5:False},nums2=[9, 4, 9, 8, 4],num=9,result=[9]
            # testcase2: map={4:True,9:True,5:False},nums2=[9, 4, 9, 8, 4],num=4,result=[9,4]
            # testcase2: map={4:True,9:True,5:False},nums2=[9, 4, 9, 8, 4],num=9,result=[9,4]
            if num in map and map[num] == False:
                # 4: その時、resultにkey値を追加。keyに対応する値をTrueに更新
                result.append(num)
                map[num] = True

        return result


if __name__ == '__main__':
    s = Solution()

    print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    print(s.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
