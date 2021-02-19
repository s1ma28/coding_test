#!/usr/bin/env python3
# *coding: utf-8

# あり得る数を全探索

import math


def solve(X):
    # i x 1.08 = Xとなる税抜き価格を求めて返す
    # in: X=432
    # out: 400

    for i in range(1, X + 1):
        if math.floor(i * 1.08) == X:
            return i

    return ':('


if __name__ == '__main__':
    # N = int(input())
    # print(solve(N))

    print(solve(432))  # 400
    print(solve(1079))  # :(
    print(solve(1001))  # 927
