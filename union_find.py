#!/usr/bin/env python3
# *coding: utf-8

def union_find():
    # parent = {0: 0, 1: 0, 2: 0, 3: 1}
    parent = {1: 1, 2: 1, 3: 2, 4: 3}

    def root(x) -> int:
        # 木の根を求める
        if parent[x] == x:   # 根
            return x
        else:
            parent[x] = root(parent[x])  # 経路圧縮。根を直接 x の親と付け直す
            return parent[x]

    def same(x, y):
        # x と y が同じ集合に属するか否か
        return root(x) == root(y)

    def unite(x, y):
        # x と yの属する集合を併合
        x = root(x)
        y = root(y)
        if x == y:
            # 同じ集合なので、スルー
            return

        # 併合
        parent[x] = y

    print(same(1, 3))
    unite(1, 3)
    print(root(3))


if __name__ == '__main__':
    union_find()
