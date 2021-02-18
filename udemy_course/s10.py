#!/usr/bin/env python3
# *coding: utf-8
from typing import List


class Solution:
    # 1単語毎の文字を逆順にして、文字列を返す
    # pre: "Let's take LeetCode contest")
    # post: "s'teL ekat edoCteeL tsetnoc"
    def reverseWords(self, s: str) -> str:
        # def reverse(s: List[str], front: int, end: int):
        #     while front < end:
        #         tmp = s[front]
        #         s[front] = s[end]
        #         s[end] = tmp
        #         front += 1
        #         end -= 1

        # corner case: 1文字の場合
        if len(s) <= 1:
            return s

        front = 0
        end = 0
        # chars = list(s)
        result = ''

        # 1: linear scan left -> right.
        while end < len(s):
            # testcase1: s='car',f=0,e=0,len(s)=3,s[end]=c => e=1
            # testcase1: s='car',f=0,e=1,len(s)=3,s[end]=a => e=2
            # testcase1: s='car',f=0,e=2,len(s)=3,s[end]=r => e=2

            # 2: endが行末なら、front-end+1をreverse()する
            if end == len(s) - 1:
                result = result + ''.join(reversed(s[front:end+1]))
                # reverse(chars, front, end)

            # 3: endが半角スペースなら、単語の切れ目なので、front～endをreverse()する
            elif s[end].isspace():
                result = result + ''.join(reversed(s[front:end])) + ' '
                # reverse(chars, front, end - 1)
                front = end + 1

            # 4: endが半角スペース or 行末でないなら、end++
            end += 1

        return result


if __name__ == '__main__':
    s = Solution()

    print(s.reverseWords("Let's take LeetCode contest"))
