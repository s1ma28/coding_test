#!/usr/bin/env python3
# *coding: utf-8


def func(i, x, a, dp):
    # base case:
    if i == 0:
        if x == 0:
            return True
        else:
            return False

    if x < 0:
        return False

    # メモをチェック
    if dp[i][x] != -1:
        return dp[i][x]

    # a[i-1]を選ばない場合
    if func(i-1, x, a, dp):
        # true をメモしてリターン
        dp[i][x] = 1
        return 1

    # a[i-1]を選ぶ場合
    if func(i-1, x-a[i-1], a, dp):
        dp[i][x] = 1
        return 1

    # どっちもダメだったらダメ
    dp[i][x] = False
    return False


if __name__ == '__main__':
    N = 5
    X = 19
    a = [3, 5, 1, 2, 9]

    MAX = 100000
    dp = [[-1] * MAX] * (N+1)
    print(func(N, 19, a, dp))
