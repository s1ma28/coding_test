#!/usr/bin/env python3
# *coding: utf-8

dp = [[0] * 499887703] * 900000


def knapsack_dp(N, w_maxlimit, v, w):

    # DPの計算
    for i in range(0, N+1):
        for b in range(w_maxlimit, -1, -1):
            if b + w[i] > w_maxlimit:
                dp[i+1][b] = dp[i][b]
            else:
                dp[i+1][b] = max(dp[i][b+w[i]] + v[i], dp[i][b])

    return dp[N][0]


if __name__ == '__main__':
    N = 30
    W = 499887702
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

    print(knapsack_dp(0, W, v, w))
