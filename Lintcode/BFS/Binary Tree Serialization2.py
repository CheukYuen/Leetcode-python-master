# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        values = [str(root.val)]
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    values.append(str(node.left.val))
                else:
                    values.append('#')
                if node.right:
                    queue.append(node.right)
                    values.append(str(node.right.val))
                else:
                    values.append('#')
        while values[-1] == '#':
            values.pop()

        return ','.join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = data.split(',')
        isLeft = True
        queue = collections.deque()
        root = TreeNode(values[0])
        queue.append(root)
        index = 0
        for val in values[1:]:
            if val != '#':
                node = TreeNode(val)
                if isLeft:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)
            if not isLeft:
                index += 1
            isLeft = not isLeft
        return root



        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

codec = Codec()
# root = codec.deserialize(codec.serialize(n1))
print codec.serialize(n1)
