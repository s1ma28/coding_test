#!/usr/bin/env python3
# *coding: utf-8

# 0～Nの間の素数をリストにして返す
def make_is_prime(N):
    # エラトステネスのふるい

    # 十分に大きい領域を確保
    primes = [0 for i in range(100000)]

    # 1: とりあえず全部ふるいに入れる
    for i in range(2, N+1):
        primes[i] = True

    for i in range(2, N+1):
        # 素数 i を発見したら
        if primes[i]:
            for j in range(i*2, N+1, i):
                primes[j] = False

    # 結果出力
    result = []
    for i in range(2, N+1):
        if primes[i]:
            result.append(i)

    return result


if __name__ == '__main__':
    N = 30
    print(make_is_prime(30))
