#!/usr/bin/env python3
# *coding: utf-8

import random


def generate_random_testcase():
    # 制約条件が以下の場合
    # 4 <= N <= 10
    # 1 <= a[i] <= 20
    # 入力形式
    # N
    # a[0] a[1] a[2] ... a[N-1]

    # N = random.randint(4, 10)
    # A = [random.randint(1, 20) for i in range(N)]

    # H = random.randint(1, 10)
    # W = random.randint(1, 10)
    H = W = 10
    field = [''.join([random.choice('xo') for i in range(W)])
             for j in range(H)]
    # s_row = random.randint(0, H-1)
    # s_col = random.randint(0, W-1)
    # g_row = random.randint(0, H-1)
    # g_col = random.randint(0, W-1)
    # field[s_row] = field[s_row][:s_col] + 's' + field[s_row][s_col+1:]
    # field[g_row] = field[g_row][:g_col] + 'g' + field[g_row][g_col+1:]

    # 英小文字をランダム生成したい場合
    # import string
    # c = random.choice(string.ascii_lowercase)

    # print(f"{H} {W}")
    for row in field:
        print(row)


if __name__ == '__main__':
    generate_random_testcase()
