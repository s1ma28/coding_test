#!/usr/bin/env python3
# *coding: utf-8

# 全探索

def solve(N):
    # 1以上N以下の整数のうち、最も2で割れる回数が多いものを求めて返す
    # ⇒ 2で最も多く掛けた際の値
    # in: N=7
    # out: 4

    i = 1
    while 2*i <= N:
        i = i * 2

    return i


if __name__ == '__main__':
    N = int(input())
    print(solve(N))

    # print(solve(7))  # 4
    # print(solve(32))  # 32
    # print(solve(100))  # 64
