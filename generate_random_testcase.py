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

    N = random.randint(4, 10)
    A = [random.randint(1, 20) for i in range(N)]

    # 英小文字をランダム生成したい場合
    # import string
    # c = random.choice(string.ascii_lowercase)

    print(N)
    print(*A)


if __name__ == '__main__':
    generate_random_testcase()
