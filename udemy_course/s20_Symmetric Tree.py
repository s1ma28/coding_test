# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 左右対称のツリー構造であるかを判定する
    # pre:
    # post:

    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetricHelper(left: TreeNode, right: TreeNode) -> bool:
            # この時点では大本の親1つは見ず、大本直下の2つの子要素から処理が始まり、孫要素同士が対象かどうかを比較する
            # base case: 子要素がないとき、再帰を終了
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            # corner case: .valの値を見る前に、nullチェックが必要。Nullpointer回避のため
            # 外側の一致を見る  ／ ＼
            if (left.left is not None and right.right is not None) and (left.left.val != right.right.val):
                return False

            # 内側の一致を見る  ＼ ／
            if (left.right is not None and right.left is not None) and (left.right.val != right.left.val):
                return False

            return isSymmetricHelper(left.left, right.right) & isSymmetricHelper(left.right, right.left)

        # base case: if root is null
        if root is None:
            return True

        # case:
        #    1
        # valの前に触れる前にNullチェック。Nullpointer回避のため。
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False

        # case: 孫要素の前に子要素の時点でsymmetricでない場合
        #    1
        #   / \
        #  2   3
        if root.left.val != root.right.val:
            return False

        # case: 孫要素の前に子要素の時点でsymmetricでない場合、再帰に入る（Top-Downアプローチ）
        #    1
        #   / \
        #  2   2
        return isSymmetricHelper(root.left, root.right)
