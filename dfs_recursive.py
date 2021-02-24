#!/usr/bin/env python3
# *coding: utf-8

def dfs(vertex_num, start, goal, G):
    seen = {x: False for x in G.keys()}

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
                print(f"{now} -> {next_v}")
                dfs_recursive(next_v, goal, G)

    dfs_recursive(start, goal, G)


if __name__ == '__main__':
    V = 7
    # E = 5
    s = 0
    t = 6
    G = {0: {1, 2}, 1: {4, 5}, 2: {3, 4}, 3: {4, 6}, 4: {6}, 5: {4, 6}, 6: {}}
    print(dfs(V, s, t, G))
