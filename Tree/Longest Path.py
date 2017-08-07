class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LongestPath:
    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left + right > self.res:
            self.res = left + right
        return max(left, right) + 1

    def main(self, root):
        if root is None:
            return 0

        self.res = 0
        self.helper(root)
        return self.res + 1


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(5)
node7 = Node(5)
node8 = Node(5)
node9 = Node(5)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
node4.left = node8
node8.left = node9
node5.right = node6
node6.right = node7

test = longestPath()
print test.main(node1)
