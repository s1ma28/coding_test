#!/usr/bin/env python3
# *coding: utf-8

# bit全探索
def bit_all_search(Ls):
    # nの数字に対して、選び方をすべての場合について考えたとき、それぞれの場合で選んだ数値の和を、さらにすべて足して和を求めて下さい。
    # in: [4, 10, 1]
    # out: 60
    # ex: {},{4},{10},{1},{4,10},{4,1},{10,1},{4,10,1}の23=8通り
    # 全部足すと、4 + 10 + 1 + 14 + 5 + 11 + 15 = 60

    sum = 0

    # 0(0b000)から7(0b111)まで。Lsの全組み合わせを一通り。
    for bit in range(1 << len(Ls)):
        for i in range(len(Ls)):
            # 配列の要素順にbitが立っていくように、maskの
            #        [4, 10, 1]
            # mask =  1        = 1 x 2^0 = 1 << 0
            # mask =  0   1    = 1 x 2^1 = 1 << 1
            # mask =  0   0  1 = 1 x 2^2 = 1 << 2
            mask = 1 << i
            if bit & mask:
                # print(Ls[i], end=' ')
                sum += Ls[i]

    return sum


if __name__ == '__main__':
    print(bit_all_search([4, 10, 1]))
