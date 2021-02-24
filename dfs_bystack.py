#!/usr/bin/env python3
# *coding: utf-8

def dfs_bystack(V, s, goal, G):

    # 既に見たノードか記録する
    seen = {}
    for i in range(V):
        seen[i] = False

    # リストを「スタック」として使用するなら、append/pop()
    # 「キュー」を使いたい場合は、「deque」使って、append/popleft()
    # from collections import deque
    # queue = deque([1, 2, 3])
    # queue.append(4)
    # queue.popleft()  # -> 1

    stack = []
    stack.append(s)  # sから探索する
    seen[s] = True

    # 深さ優先探索
    while len(stack) != 0:  # 探索リストが残っている限り続行
        # 現在の位置
        state = stack.pop()
        seen[state] = True
        if state != goal:
            neightbors = G[state]
            for next in neightbors:
                if seen[next] == False:  # 未探索なら、探索リストに追加する
                    # seen[next] = True
                    stack.append(next)
                    print(f"{state} -> {next}")

    # if seen[goal]:
    #     return True
    # else:
    #     return False


if __name__ == '__main__':
    V = 7
    # E = 5
    s = 0
    t = 6
    G = {0: {1, 2}, 1: {4, 5}, 2: {3, 4}, 3: {4, 6}, 4: {6}, 5: {4, 6}}
    print(dfs_bystack(V, s, t, G))
