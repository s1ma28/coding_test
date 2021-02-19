#!/usr/bin/env python3
# *coding: utf-8

def dfs(V, E, s, goal, G):

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
        if state != goal:
            next = G[state]
            if seen[next] == False:  # 未探索なら、探索リストに追加する
                seen[next] = True
                stack.append(next)

    if seen[goal]:
        return True
    else:
        return False


if __name__ == '__main__':
    V = 4
    E = 5
    s = 0
    t = 3
    G = {0: 1, 0: 2, 1: 3, 2: 1, 2: 3}
    print(dfs(V, E, s, t, G))
