#!/usr/bin/env python3
# *coding: utf-8

# あり得る数を全探索


def solve(A, B, C, X, Y):
    # AピザX枚とBピザY枚を買うのに、最小のコストを求めて返す
    # in: 1500, 2000, 1600, 3, 2
    # out: 7900

    if A + B < 2 * C:
        # Aピザ、Bピザを単独で買った方が安い
        return A * X + B * Y
    else:
        # パターン1: 先にCセットをできるだけ買って、足りない分は買い足す
        mi = min(X, Y)
        cost1 = 0
        if X < Y:
            # AB枚数 + B枚数
            cost1 = 2*C * mi + B * (Y-mi)
        else:
            # AB枚数 + A枚数、X=Y のとき
            cost1 = 2*C * mi + A * (X-mi)

        # パターン2: 全部Cセットでそろえる。（余分なピザが出てもかまわない）
        ma = max(X, Y)
        cost2 = 2*C * ma

    return min(cost1, cost2)


if __name__ == '__main__':
    # A, B, C, X, Y = map(int, input().split())
    # print(solve(A, B, C, X, Y))

    print(solve(1500, 2000, 1600, 3, 2))  # 7900
    print(solve(1500, 2000, 1900, 3, 2))  # 7900
    print(solve(1500, 2000, 500, 90000, 100000))  # 7900
