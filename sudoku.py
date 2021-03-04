#!/usr/bin/env python3
# *coding: utf-8


from typing import Reversible


def recursive(field, result):
    # result に見つかった答えを格納する,
    # 答えが一つとは限らないので result はリストにする

    # 空きマスを探す
    empty_row = empty_col = -1
    row = col = 0
    while row < 9 and empty_row == -1:
        while col < 9 and empty_col == -1:
            if field[row][col] == -1:
                # 空きマス発見
                empty_row = row
                empty_col = col
                break

            col += 1

        row += 1

    # 再帰終了状況: すべて埋まって飽きマスがない
    if empty_row == -1 or empty_col == -1:
        result.append(field)
        return

    # 空きマスに入れられる数字を求める。
    # canuse[] == True : 入れられる
    # canuse[] == False : 入れられない。既に使われているため。
    canuse = [True for x in range(10)]
    for x in range(10):
        # 同じ列に同じ数字はダメ
        if field[empty_row][x] != -1:
            canuse[field[empty_row][x]] = False

        # 同じ行に同じ数字はダメ
        if field[x][empty_col] != -1:
            canuse[field[x][empty_col]] = False

        # 同じブロックの中央を求める
        center_row = empty_row / 3 * 3 + 1
        center_col = empty_col / 3 * 3 + 1
        # 同じブロックに同じ数字はダメ
        for row in range(center_row-1, center_row+2):
            for col in range(center_col-1, center_col+2):
                if field[row][col] != -1:
                    canuse[field[row][col]] = False

    # 再帰的に探索
    for v in range(1, 10):
        if canuse[v] != False:
            continue

        # 空きマスに数値 vを置く
        field[empty_row][empty_col] = v

        krecursive(field, result)

    # 数値を置いていた空きマスを元の空きマスに戻す（この処理をバックトラックと呼ぶ）
    field[empty_row][empty_col] = -1


if __name__ == '__main__':
    field = []
    for row in range(9):
        line = input()
        for col in range(9):
            cell = None
            if line[col] == '*':
                # '*' ： 埋めるマスのマーク
                cell = line[col]
            else:
                # char'0'～'9' ⇒ int 0～9にする
                cell = int(line[col])

            field[row][col].append(cell)

    # 再帰的に解く
    result = []
    recursive(field, result)

    import copy
    # 答えを出力する
    if len(result) == 0:
        print("no solutions.")
    elif len(result) > 1:
        print("more than one solutions.")
    else:
        ans = result[0]
        for row in range(9):
            for col in range(9):
                print(f"{ans[row][col]} ", end='')

            print()
