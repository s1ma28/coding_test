
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 共通する先祖の最短を求めて返す。BSTなので、ソート前提。
    # pre: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    # post: 6
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowestCommonAncestorRecursive(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            # base case: if root.val is p.val or q.val, then root is LCA so return root
            if root.val == p.val or root.val == q.val:
                return root

            # step 1: if min(p.val, q.val) < root.val < max(p.val, q.val), then root is LCA as well
            if min(p.val, q.val) < root.val and root.val < max(p.val, q.val):
                return root

            # step 2: if max(p.val, q.val) < root.val, recurse left subtree
            if p.val < root.val and q.val < root.val:
                # if max(p.val, q.val) < root.val:
                return lowestCommonAncestorRecursive(root.left, p, q)

            # step 3: else if root.val < min(p.val, q.val), recurse right subtree
            if root.val < p.val and root.val < q.val:
                # if min(p.val, q.val) > root.val:
                return lowestCommonAncestorRecursive(root.right, p, q)

        return lowestCommonAncestorRecursive(root, p, q)
