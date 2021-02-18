#!/usr/bin/env python3
# *coding: utf-8

# 全探索

def solve(N):
    # N以下の正の整数のうち、(先頭に0をつけずに十進法で表記したときの) 桁数が奇数であるようなものの個数を求めて返す
    # in: N=11
    # out: 9

    cnt = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            cnt += 1

    return cnt


if __name__ == '__main__':
    N = int(input())
    print(solve(N))

    # print(solve(11))  # 9
    # print(solve(136))  # 46
    # print(solve(100000))  # 90909
