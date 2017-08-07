# Definition for a binary tree node.
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p, q):
    if not p and q:
        return False
    if p and not q:
        return False
    if not p and not q:
        return True
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
