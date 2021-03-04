#!/usr/bin/env python3
# *coding: utf-8

def dfs(seen, start, goal, G):

    def dfs_recursive(now, goal, G):

        # now を訪問済みにする
        seen[now] = True

        # now から行ける各頂点 next_v について
        for next_v in G[now]:
            if seen[next_v] == True:
                # next_vが探索済みだったらスルー
                continue
            else:
                # 探索済みでないなら、再帰的に探索
                # print(f"{now} -> {next_v}")
                dfs_recursive(next_v, goal, G)

    dfs_recursive(start, goal, G)


if __name__ == '__main__':
    # V = 7
    # E = 5
    s = 0
    t = 6
    G = {0: {1, 2}, 1: {4, 5}, 2: {3, 4}, 3: {4, 6}, 4: {6}, 5: {4, 6}, 6: {}}

    # 全頂点を「未訪問」に初期化
    seen = {x: False for x in G.keys()}

    # 頂点 sをスタートとした探索
    print(dfs(seen, s, t, G))

    # t 辿りつけるかどうか
    if seen[t] == True:
        print("Yes reached.")
    else:
        print("No reach.")
