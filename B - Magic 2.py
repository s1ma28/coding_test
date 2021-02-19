#!/usr/bin/env python3
# *coding: utf-8

# あり得る数を全探索

import math


def solve(red, green, blue, K):
    # 以下ルールを同時に満たす、魔術を成功できるかの判定結果を返す
    #   - 緑のカードに書かれている整数は、赤のカードに書かれている整数より真に大きい。
    #   - 青のカードに書かれている整数は、緑のカードに書かれている整数より真に大きい。
    # in: X=432
    # out: 400

    cards = {'r': red, 'g': green, 'b': blue}

    for i in range(K):
        if cards['b'] <= cards['g'] or cards['b'] <= cards['r']:
            cards['b'] *= 2
        elif cards['g'] <= cards['r']:
            cards['g'] *= 2

        # 魔術が成功するか判定
        if cards['g'] > cards['r'] and cards['b'] > cards['g']:
            return 'Yes'

    # 魔術をK回実施しても成功しなかったので、False
    return 'No'


if __name__ == '__main__':
    # A, B, C = map(int, input().split())
    # K = int(input())
    # print(solve(red=A, green=B, blue=C, K=K))

    print(solve(red=7, green=2, blue=5, K=3))  # Yes
    print(solve(red=7, green=4, blue=2, K=3))  # No
