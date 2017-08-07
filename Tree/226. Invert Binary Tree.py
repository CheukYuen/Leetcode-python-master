class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None
    left = root.left
    right = root.right
    root.left = invertTree(right)
    root.right = invertTree(left)
    return root

