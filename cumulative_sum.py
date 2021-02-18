#!/usr/bin/env python3
# *coding: utf-8

infinity = float('INF')


def cumulative_sum(N, K, a):
    # 累積和を使って、区間の最大値を返す
    # in: N=5, K=3, a=[2,5,-4,10,3]
    # out: 11

    # 累積和を前計算
    s = [0 for i in range(N+1)]
    for i in range(N):
        s[i+1] = s[i] + a[i]

    # 答えを求める
    # 最初は無限小の値に初期化しておく
    res = -infinity
    for i in range(N-K + 1):
        val = s[K+i] - s[i]
        if res < val:
            res = val

    return res


if __name__ == '__main__':
    # 入力
    N, K = [int(x) for x in input().split()]
    a = []
    for i in range(N):
        a.append(int(input()))

    print(cumulative_sum(N, K, a))
