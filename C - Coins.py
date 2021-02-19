#!/usr/bin/env python3
# *coding: utf-8

# 再帰による全探索 での解法が見当たらなかった。

from itertools import combinations


def solve(N, K, A):
    coins = []
    for i in range(10):
        coins.append(5*10**(9-i))
        coins.append(10**(9-i))

    # 商品の全組合せ
    Ls = list(combinations(A, K))
    out = 10**9
    for L in Ls:
        # 合計金額を算出
        S = sum(L)
        cand = 0
        for coin in coins:
            # 7000 / 1000 = 7枚 というわけで引き算ではなく割り算使うと計算が一発
            cand += S//coin
            # 割り算したときの余りが次に計算するもの
            S = S % coin
        out = min(cand, out)

    return (out)


if __name__ == '__main__':
    # N, M, Q = map(int, input().split())
    # a_b_c_d = []
    # for i in range(Q):
    #     a_b_c_d.append(tuple(map(int, input().split())))

    N = 3
    K = 2
    print(recursive_search(N, K, [25, 29, 62]))
