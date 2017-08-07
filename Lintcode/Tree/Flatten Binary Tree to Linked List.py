"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        self.helper(root)

    def helper(self, root):
        if root is None:
            return None
        leftLast = self.helper(root.left)
        rightLast = self.helper(root.right)

        if leftLast:
            leftLast.right = root.right
            root.right = root.left
            root.left = None

        if rightLast:
            return rightLast

        if leftLast:
            return leftLast
        return root

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node8 = TreeNode(8)

node1.left = node2
node2.left = node3
node2.right = node4
node1.right = node5
node5.right = node6
node4.left = node8
test = Solution()
test.flatten(node1)


