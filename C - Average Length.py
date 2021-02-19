#!/usr/bin/env python3
# *coding: utf-8

# 順列全探索

def permutation_all_search(N, x_y):
    import itertools
    import math
    from functools import reduce

    sums = []
    for row in itertools.permutations(range(1, N+1)):
        sum = 0
        for j in range(N-1):
            # (xi - xj)^2 + (yi - yj)^2
            tmp = (x_y[row[j]][0] - x_y[row[j+1]][0])**2 + \
                (x_y[row[j]][1] - x_y[row[j+1]][1])**2
            sum += math.sqrt(tmp)

        sums.append(sum)

    # 平均値を出す
    result = reduce(lambda a, b: a+b, sums)
    average = result / len(sums)

    return average


if __name__ == '__main__':
    N = int(input())
    x_y = {}
    for i in range(1, N+1):
        x, y = map(int, input().split())
        x_y[i] = (x, y)
    # N = 3
    # x_y = {1: (0, 0), 2: (1, 0), 3: (0, 1)}
    print(permutation_all_search(N, x_y))
