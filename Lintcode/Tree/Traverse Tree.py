class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse(root, res):
    if root is None:
        return None
    result = []
    left = traverse(root.left)
    right = traverse(root.right)

    if left:
        result += left

    result.append(root.val)

    if right:
        result += right

    return result


n4 = TreeNode(4)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4.left = n1
n1.left = n2
n1.right = n3

traverse(n4, res)

print res

#
# def dfs(root, result):
#     if root is None:
#         return
#     dfs(root.left, result)
#
#     dfs(root.right, result)
#     result.append(root.val)
