#!/usr/bin/env python3
# *coding: utf-8


def knapsack(things_num, weight_maxlimit, v, w):
    memo = [[0] * (weight_maxlimit + 1)] * (things_num + 1)

    def knapsack_rec(things_i, remaining_space, v, w):
        if memo[things_i][remaining_space] != 0:
            # 既に計算したことあるなら再利用
            return memo[things_i][remaining_space]

        result = None
        if things_i == things_num:
            result = 0
        elif remaining_space < w[things_i]:
            # 残りスペースが現在の品物より小さいなら、そもそも選べないので選ばない場合を結果として保存
            result = knapsack_rec(things_i + 1, remaining_space, v, w)
        else:
            # 現在の品物を選ぶ場合で再帰
            use = knapsack_rec(things_i+1, remaining_space -
                               w[things_i], v, w) + v[things_i]

            # 現在の品物を選ばない場合で再帰
            no_use = knapsack_rec(things_i+1, remaining_space, v, w)

            # 品物の価値の合計が大きい方を結果として保存
            result = max(use, no_use)

        # 結果をメモ
        memo[things_i][remaining_space] = result
        return result

    return knapsack_rec(0, weight_maxlimit, v, w)


if __name__ == '__main__':
    things_num = 30
    weight_maxlimit = 499887702
    input_line = '''128990795 137274936
575374246 989051853
471048785 85168425
640066776 856699603
819841327 611065509
704171581 22345022
536108301 678298936
119980848 616908153
117241527 28801762
325850062 478675378
623319578 706900574
998395208 738510039
475707585 135746508
863910036 599020879
340559411 738084616
122579234 545330137
696368935 86797589
665665204 592749599
958833732 401229830
371084424 523386474
463433600 5310725
210508742 907821957
685281136 565237085
619500108 730556272
88215377 310581512
558193168 136966252
475268130 132739489
303022740 12425915
122379996 137199296
304092766 23505143
'''
    v = []
    w = []
    for row in input_line.split('\n'):
        if row != '':
            tmp = row.split()
            v.append(int(tmp[0]))
            w.append(int(tmp[1]))

    print(knapsack(things_num, weight_maxlimit, v, w))
