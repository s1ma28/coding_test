#!/usr/bin/env python3
# *coding: utf-8


if __name__ == '__main__':
    N, M = map(int, input().split())
    Ks = []

    for i in range(M):
        row = input()
        k = int(row[0])
        s = list(map(int, row[1:].split()))
        Ks.append((k, s))

    P = list(map(int, input().split()))

    ans = 0
    for i in range(1 << N):
        counter = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                for k in range(M):
                    if j+1 in Ks[k][1]:
                        counter[k] += 1
        ok = True
        for k in range(M):
            if counter[k] % 2 == P[k]:
                ok = ok & True
            else:
                ok = ok & False

        if ok:
            ans += 1

    print(ans)
