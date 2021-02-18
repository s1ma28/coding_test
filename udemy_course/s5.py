#!/usr/bin/env python3
# *coding: utf-8

from typing import List


class Solution:

    # 配列の要素を逆順に変換する。新規の配列は作成NG
    # pre: ["h", "e", "l", "l", "o"]
    # post: ["o","l","l","e","h"]
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # step1: arrayを両端から1ずつ取得する
        front = 0
        end = len(s) - 1
        while front < end:
            # step2: 要素を入れ換える。i, i-1 = i-1, i
            s[front], s[end] = s[end], s[front]

            front += 1
            end -= 1

        return s


if __name__ == '__main__':
    s = Solution()

    print(s.reverseString(["h", "e", "l", "l", "o"]))
    print(s.reverseString(["H", "a", "n", "n", "a", "h"]))
