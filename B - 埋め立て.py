#!/usr/bin/env python3
# *coding: utf-8

import sys
sys.setrecursionlimit(10**7)
field = []


def dfs(now_row, now_col):
    cnt = 0
    # 現在のマスが'o'なら、カウント+1して、'x'に変更
    if field[now_row][now_col] == 'o':
        cnt = 1
        field[now_row] = field[now_row][:now_col] + \
            'x' + field[now_row][now_col+1:]

    # 再帰終了case: 4方向を全て探索したとき。
    # 今回の定義：「つながっている」＝上下左右で隣接。斜めはスルー
    for next_row, next_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_row = now_row + next_row
        new_col = now_col + next_col

        # 場外アウト、またはそのマスが「×」ならスルー。再帰するまでもなし。
        if not(0 <= new_row < 10) or not(0 <= new_col < 10) or field[new_row][new_col] == 'x':
            continue

        # 「o」ならそのマスを中心に再帰。
        # 今回マスの結果 + 周辺マスの結果
        cnt += dfs(new_row, new_col)

    return cnt


if __name__ == '__main__':
    field = []
    max_cell = 0
    for row in range(10):
        tmp = input()
        max_cell += tmp.count('o')
        field.append(tmp)

    import copy
    orig_field = copy.deepcopy(field)
    count = 0
    for row in range(10):
        for col in range(10):
            count = 0
            count = dfs(row, col)

            # 現在マスを中心に再帰した結果、「o」に辿れたマスの数が一致していれば、
            # 1つの島にできるということでYesを返す
            if count == max_cell:
                print('YES')
                sys.exit()

            # 探索済みとして'x'を'o'に変えていたので、元々の入力データに戻す
            field = copy.deepcopy(orig_field)

    print('NO')
