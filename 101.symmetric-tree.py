# recuresive
class Solution(object):
    def isSymmetric(self, root):
        if not root:    
            return True
        else:
            return isMirror(root.left, root.right)
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                return isMirror(left.left, right.right) == isMirror(left.right, right.left)
            else:
                return False

# iterative
class Solution(object):
    def isSym(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]
        while len(stack) > 0:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
