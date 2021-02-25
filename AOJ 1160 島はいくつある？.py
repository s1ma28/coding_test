#!/usr/bin/env python3
# *coding: utf-8

import sys
sys.setrecursionlimit(10**7)

H = W = None
field = []


def dfs(now_row, now_col):

    # 探索済みのマスは、「白」にする。 （数えない方とか障害物の方とかの値にするんだな）
    field[now_row][now_col] = 0

    # 八方向を探索。8方向を全部探索したら現在分の関数終了。
    for next_row in range(-1, 2):
        for next_col in range(-1, 2):
            new_row = now_row + next_row
            new_col = now_col + next_col

            # 場外アウトや、「白」マスだったらスルー
            if not(0 <= new_row < H) or not(0 <= new_col < W) or field[new_row][new_col] == 0:
                continue

            # 新しく見つかった「黒」マスを中心に、8方向、再帰的に探索
            dfs(new_row, new_col)


if __name__ == '__main__':
    while True:
        W, H = map(int, input().split())
        if H == 0 or W == 0:
            break

        field = []
        for row in range(H):
            field.append([])
            for e in input().split():
                field[row].append(int(e))

        # 探索開始
        count = 0
        for row in range(H):
            for col in range(W):
                if field[row][col] == 0:
                    # 現在のマスが島じゃなかったらスルー
                    continue

                # 「白」：開封済み。カウント対象外。
                # 「黒」：未開封。カウント対象。カウントしたら「白」に変更
                # 現在のマスが島なら、周り(8方向)を探索
                dfs(row, col)
                count += 1

        print(count)
