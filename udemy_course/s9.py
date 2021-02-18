#!/usr/bin/env python3
# *coding: utf-8
from typing import Awaitable, List


class Solution:
    # 2つの文字列がアナグラムになっているかチェック
    # pre: s="anagram", t="nagaram"
    # post: True

    def isAnagram(self, s: str, t: str) -> bool:
        # corner case: s or t is null, not an
        if not s and not t:
            return True
        if not s or not t:
            return False

        # 1: 長さが同じかチェック。異なっていたらreturn False
        if len(s) != len(t):
            return False

        # 2: 文字列をmap化する(文字, 出現回数)
        s_map = self._string_to_dict(s)
        t_map = self._string_to_dict(t)

        # 3: 2つのmapのkeyとcountが全て一致したら、アナグラム。return True
        if s_map == t_map:
            return True

    def _string_to_dict(self, s: str) -> dict:
        map = {}
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1

        return map


if __name__ == '__main__':
    s = Solution()

    print(s.isAnagram(s="anagram", t="nagaram"))
    print(s.isAnagram(s="rat", t="car"))
