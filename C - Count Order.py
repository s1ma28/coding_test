#!/usr/bin/env python3
# *coding: utf-8

# 順列全探索

def permutation_all_search(N, P, Q):
    import itertools
    import math
    from functools import reduce

    # corner case: P と Qが同じ場合は、|a - b| = 0なので
    if P == Q:
        return 0

    p_i = q_i = 0
    # 順列全列挙
    for i, row in enumerate(itertools.permutations(range(1, N+1))):
        # PやQと一致する際の番号を取得
        if row == P:
            p_i = i + 1
        elif row == Q:
            q_i = i + 1

    # 番号の差分を計算し、絶対値
    return abs(p_i - q_i)


if __name__ == '__main__':
    # N = 3
    N = int(input())
    P = map(int, input().split())
    Q = map(int, input().split())
    # print(permutation_all_search(3, tuple([1, 3, 2]), tuple([3, 1, 2])))
    print(permutation_all_search(N, tuple(P), tuple(Q)))
