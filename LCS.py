#!/usr/bin/env python3
# *coding: utf-8`

def LCS(str1, str2) -> int:
    # 最長共通部分列の数をDPで計算し、返す
    # Longest Common Subsequence
    # in: str1='myabcuuu', str2='abcjju'
    # out: 4 (最長部分列はabcu)

    # 0で初期化
    dp = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]

    for i in range(len(str2)):
        for j in range(len(str1)):
            if str1[j] == str2[i]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    # 表の右下の値を返す
    return dp[-1][-1]


if __name__ == '__main__':
    print(LCS(str1='myabcuuu', str2='abcjju'))
