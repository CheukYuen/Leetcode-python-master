import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def serialize(root):
    # write your code here
    if not root:
        return []
    queue = collections.deque()
    queue.append(root)
    index = 0
    while index < len(queue):
        if queue[index]:
            queue.append(queue[index].left)
            queue.append(queue[index].right)
        index += 1
    while queue[-1] is None:
        queue.pop()
    result = []
    for i in range(len(queue)):
        if queue[i]:
            result.append(str(queue[i].val))
        else:
            result.append('#')
    return ','.join(result)



def deserialize(data):
    if not data:
        return None
    vals = data.split(',')
    queue = collections.deque()
    root = TreeNode(vals[0])
    queue.append(root)
    isLeft = True
    index = 0
    for val in vals[1:]:
        if val != '#':
            node = TreeNode(val)
            if isLeft:
                queue[index].left = node
            else:
                queue[index] = node
            queue.append(node)
        if not isLeft:
            index += 1
        isLeft = not isLeft
    return root






n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
print serialize(n1)
