class TreeNode:
    def __init__(self, val):
        self.val = val


class Node:
    def __init__(self, size, sumVal):
        self.size = size
        self.sumVal = sumVal


def findSubtree2(root):
    if root is None:
        return None

    maxSumz = [float('-inf')]
    resultNode = [None]

    helper(root, maxSumz, resultNode)
    return resultNode[0]


def helper(root, maxSumz, resultNode):
    if root is None:
        return Node(0, 0)
    left = helper(root.left)
    right = helper(root.right)

    size = left.size + right.size + 1
    sumVal = left.sumVal + right.sumVal + root.val

    if sumVal / size > maxSumz:
        resultNode[0] = root
        maxSumz[0] = left.sumVal + right.sumVal + root.val

    return Node(left.sumVal + right.sumVal + root.val, root)
