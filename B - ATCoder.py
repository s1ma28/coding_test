#!/usr/bin/env python3
# *coding: utf-8

def rep(s):
    # sの部分文字列でACGTのみを含む文字列の、最長の長さを返す
    # in: s='ATCODER'
    # out: 3
    ans = 0
    tmp = 0

    for char in s:
        if char == 'A' or char == 'T' or char == 'G' or char == 'C':
            tmp += 1
            ans = max(tmp, ans)
        else:
            tmp = 0

    return ans


if __name__ == '__main__':

    s = input()

    print(rep(s))
