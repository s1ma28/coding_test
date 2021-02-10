class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 重複していない文字がいくつあるかを返す
        # pre: "leetcode"
        # post: int(total char count)

        # s が1以下の場合、既にuniqueなので先頭の位置0を返す
        if len(s) == 1:
            return 0

        char_map = {}
        # 1. ArrayをMap化する
        for c in s:
            # 2. 同じ文字が既にMapにあるなら、countを+1する
            if c in char_map.keys():
                char_map[c] += 1
            else:
                char_map[c] = 1

        # 3. 再度Arrayから要素を順に取得し、keyとしてMapの値を取得する
        for i, c in enumerate(s):
            if char_map[c] == 1:
                # 4. Mapの値が1なら、そのときのindex値を返して終了
                return i

        # ユニークの値がなかった場合、-1を返して終了
        return -1
