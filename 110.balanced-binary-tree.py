# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        self.isBalanced = True
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if not self.isBalanced or abs(left - right) > 1:
                self.isBalanced = False
            return max(left, right) + 1

        dfs(root)
        return self.isBalanced



# basic
class Solution2(object):
    def isBala(self, root):
        def td(node):
            if not node:
                return 0
            lf = td(node.left)
            rt = td(node.right)
            return max(lf, rt) + 1

        if not root:
            return True
        left = td(node.left)
        right = td(node.right)
        if abs(left - right)>1:
            return False
        return self.isBala(root.left) and self.isBala(root.rigjt)