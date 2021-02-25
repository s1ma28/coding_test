#!/usr/bin/env python3
# *coding: utf-8

import sys
sys.setrecursionlimit(10**7)
# 四方向への移動ベクトル
#          下, 上, 右, 左
move_row = [1, -1, 0, 0]
move_col = [0, 0, 1, -1]


def dfs(field, H, W, now_row, now_col):

    # 再帰終了case: 場外アウトや、移動先が壁の状況
    if not(0 <= now_row < H) or not(0 <= now_col < W) or field[now_row][now_col] == '#':
        return

    # 現在のマスがゴールの場合、探索自体終了。（枝切り）
    if field[now_row][now_col] == 'g':
        print('Yes')
        sys.exit()

    # 現在マスを訪問済みにする ⇒ seen配列を使うとメモリを結構食うので、現在マスを'#'にすることで「探索しなくていい」とマークする
    # seen[now_row][now_col] = True
    field[now_row][now_col] = '#'

    # 四方向を探索
    for next in range(4):
        new_row = now_row + move_row[next]
        new_col = now_col + move_col[next]

        # 再帰的に探索
        dfs(field, H, W, new_row, new_col)

    return

# return seen[goal_row][goal_col]


if __name__ == '__main__':
    H, W = map(int, input().split())
    field = [list(input()) for x in range(H)]

    # start と goal のマスを特定する
    start_row = start_col = goal_row = goal_col = None
    for row in range(H):
        for col in range(W):
            if field[row][col] == 's':
                start_row = row
                start_col = col
            # elif field[row][col] == 'g':
            #     goal_row = row
            #     goal_col = col

    # seen 配列全体をFalseで初期化 ⇒ メモリを食うので使わない方針に変更
    # seen = [[False for col in range(W)] for row in range(H)]

    # 探索開始
    dfs(field, H, W, start_row, start_col)

    print('No')
