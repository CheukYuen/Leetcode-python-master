class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    if root is None:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.left = node4

print maxDepth(node1)